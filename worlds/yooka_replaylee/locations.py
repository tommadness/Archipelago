from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ReplayleeWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    "TT - Quill 0": 1,
    "TT - Quill 1": 2,
    "TT - Quill 2": 3,
    "TT - Quill 3": 4,
    "TT - Quill 4": 5,
    "TT - Quill 5": 6,
    "TT - Quill 6": 7,
    "TT - Quill 7": 8,
    "TT - Quill 8": 9,
    "TT - Quill 9": 10,
    "TT - Quill 10": 11,
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class YookaReplayleeLocation(Location):
    game = "YookaReplaylee"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: ReplayleeWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: ReplayleeWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    ht_entrance = world.get_region("Hivory Towers Entrance")
    ht_near_tt = world.get_region("Hivory Towers Near TT")
    tt_start_island = world.get_region("Tribalstack Tropics Starting Island")

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    tt_quill_locations = get_location_names_with_ids(
        ["TT - Quill 0", "TT - Quill 1", "TT - Quill 2", "TT - Quill 3", "TT - Quill 4", "TT - Quill 5", "TT - Quill 6", "TT - Quill 7", "TT - Quill 8", "TT - Quill 9", "TT - Quill 10"]
    )
    tt_start_island.add_locations(tt_quill_locations, YookaReplayleeLocation)

    # Locations may be in different regions depending on the player's options.
    # In our case, the hammer option puts the Top Middle Chest into its own room called Top Middle Room.
    """ top_middle_room_locations = get_location_names_with_ids(["Top Middle Chest"])
    if world.options.hammer:
        top_middle_room = world.get_region("Top Middle Room")
        top_middle_room.add_locations(top_middle_room_locations, YookaReplayleeLocation)
    else:
        overworld.add_locations(top_middle_room_locations, YookaReplayleeLocation)
 """
    # Locations may exist only if the player enables certain options.
    # In our case, the extra_starting_chest option adds the Bottom Left Extra Chest location.
    """ if world.options.extra_starting_chest:
        # Once again, it is important to stress that even though the Bottom Left Extra Chest location doesn't always
        # exist, it must still always be present in the world's location_name_to_id.
        # Whether the location actually exists in the seed is purely determined by whether we create and add it here.
        bottom_left_extra_chest = get_location_names_with_ids(["Bottom Left Extra Chest"])
        overworld.add_locations(bottom_left_extra_chest, YookaReplayleeLocation)
 """

def create_events(world: ReplayleeWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    tt_start_island = world.get_region("Tribalstack Tropics Starting Island")
    tt_near_shovel_knight = world.get_region("Tribalstack Tropics Near Shovel Knight")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    tt_pot_event = YookaReplayleeLocation(world.player, "Completed Pot Event", None, tt_start_island)
    tt_start_island.locations.append(tt_pot_event)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    tt_pot_item = items.ReplayleeItem("Completed Pot Event", ItemClassification.progression, None, world.player)
    tt_pot_event.place_locked_item(tt_pot_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    tt_near_shovel_knight.add_event(
        "Final Boss Defeated", "Victory", location_type=YookaReplayleeLocation, item_type=items.ReplayleeItem
    )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
