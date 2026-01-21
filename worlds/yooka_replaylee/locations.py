from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import ReplayleeWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
HT_ID = 00000
TT_ID = 10000
QUILL_ID = 00000
PAGIE_ID = 1000
LOCATION_NAME_TO_ID = {
    # Tribalstack Tropics - Quills
    "TT - Quill 0": TT_ID + QUILL_ID + 0,
    "TT - Quill 1": TT_ID + QUILL_ID + 1,
    "TT - Quill 2": TT_ID + QUILL_ID + 2,
    "TT - Quill 3": TT_ID + QUILL_ID + 3,
    "TT - Quill 4": TT_ID + QUILL_ID + 4,
    "TT - Quill 5": TT_ID + QUILL_ID + 5,
    "TT - Quill 6": TT_ID + QUILL_ID + 6,
    "TT - Quill 7": TT_ID + QUILL_ID + 7,
    "TT - Quill 8": TT_ID + QUILL_ID + 8,
    "TT - Quill 9": TT_ID + QUILL_ID + 9,
    "TT - Quill 10": TT_ID + QUILL_ID + 10,
    "TT - Quill 11": TT_ID + QUILL_ID + 11,
    "TT - Quill 12": TT_ID + QUILL_ID + 12,
    "TT - Quill 13": TT_ID + QUILL_ID + 13,
    "TT - Quill 14": TT_ID + QUILL_ID + 14,
    "TT - Quill 15": TT_ID + QUILL_ID + 15,
    "TT - Quill 16": TT_ID + QUILL_ID + 16,
    "TT - Quill 17": TT_ID + QUILL_ID + 17,
    "TT - Quill 18": TT_ID + QUILL_ID + 18,
    "TT - Quill 19": TT_ID + QUILL_ID + 19,
    "TT - Quill 20": TT_ID + QUILL_ID + 20,
    "TT - Quill 21": TT_ID + QUILL_ID + 21,
    "TT - Quill 22": TT_ID + QUILL_ID + 22,
    "TT - Quill 23": TT_ID + QUILL_ID + 23,
    "TT - Quill 24": TT_ID + QUILL_ID + 24,
    "TT - Quill 25": TT_ID + QUILL_ID + 25,
    "TT - Quill 26": TT_ID + QUILL_ID + 26,
    "TT - Quill 27": TT_ID + QUILL_ID + 27,
    "TT - Quill 28": TT_ID + QUILL_ID + 28,
    "TT - Quill 29": TT_ID + QUILL_ID + 29,
    "TT - Quill 30": TT_ID + QUILL_ID + 30,
    "TT - Quill 31": TT_ID + QUILL_ID + 31,
    "TT - Quill 32": TT_ID + QUILL_ID + 32,
    "TT - Quill 33": TT_ID + QUILL_ID + 33,
    "TT - Quill 34": TT_ID + QUILL_ID + 34,
    "TT - Quill 35": TT_ID + QUILL_ID + 35,
    "TT - Quill 36": TT_ID + QUILL_ID + 36,
    "TT - Quill 37": TT_ID + QUILL_ID + 37,
    "TT - Quill 38": TT_ID + QUILL_ID + 38,
    "TT - Quill 39": TT_ID + QUILL_ID + 39,
    "TT - Quill 40": TT_ID + QUILL_ID + 40,
    "TT - Quill 41": TT_ID + QUILL_ID + 41,
    "TT - Quill 42": TT_ID + QUILL_ID + 42,
    "TT - Quill 43": TT_ID + QUILL_ID + 43,
    "TT - Quill 44": TT_ID + QUILL_ID + 44,
    "TT - Quill 45": TT_ID + QUILL_ID + 45,
    "TT - Quill 46": TT_ID + QUILL_ID + 46,
    "TT - Quill 47": TT_ID + QUILL_ID + 47,
    "TT - Quill 48": TT_ID + QUILL_ID + 48,
    "TT - Quill 49": TT_ID + QUILL_ID + 49,
    "TT - Quill 50": TT_ID + QUILL_ID + 50,
    "TT - Quill 51": TT_ID + QUILL_ID + 51,
    "TT - Quill 52": TT_ID + QUILL_ID + 52,
    "TT - Quill 53": TT_ID + QUILL_ID + 53,
    "TT - Quill 54": TT_ID + QUILL_ID + 54,
    "TT - Quill 55": TT_ID + QUILL_ID + 55,
    "TT - Quill 56": TT_ID + QUILL_ID + 56,
    "TT - Quill 57": TT_ID + QUILL_ID + 57,
    "TT - Quill 58": TT_ID + QUILL_ID + 58,
    "TT - Quill 59": TT_ID + QUILL_ID + 59,
    "TT - Quill 60": TT_ID + QUILL_ID + 60,
    "TT - Quill 61": TT_ID + QUILL_ID + 61,
    "TT - Quill 62": TT_ID + QUILL_ID + 62,
    "TT - Quill 63": TT_ID + QUILL_ID + 63,
    "TT - Quill 64": TT_ID + QUILL_ID + 64,
    "TT - Quill 65": TT_ID + QUILL_ID + 65,
    "TT - Quill 66": TT_ID + QUILL_ID + 66,
    "TT - Quill 67": TT_ID + QUILL_ID + 67,
    "TT - Quill 68": TT_ID + QUILL_ID + 68,
    "TT - Quill 69": TT_ID + QUILL_ID + 69,
    "TT - Quill 70": TT_ID + QUILL_ID + 70,
    "TT - Quill 71": TT_ID + QUILL_ID + 71,
    "TT - Quill 72": TT_ID + QUILL_ID + 72,
    "TT - Quill 73": TT_ID + QUILL_ID + 73,
    "TT - Quill 74": TT_ID + QUILL_ID + 74,
    "TT - Quill 75": TT_ID + QUILL_ID + 75,
    "TT - Quill 76": TT_ID + QUILL_ID + 76,
    "TT - Quill 77": TT_ID + QUILL_ID + 77,
    "TT - Quill 78": TT_ID + QUILL_ID + 78,
    "TT - Quill 79": TT_ID + QUILL_ID + 79,
    "TT - Quill 80": TT_ID + QUILL_ID + 80,
    "TT - Quill 81": TT_ID + QUILL_ID + 81,
    "TT - Quill 82": TT_ID + QUILL_ID + 82,
    "TT - Quill 83": TT_ID + QUILL_ID + 83,
    "TT - Quill 84": TT_ID + QUILL_ID + 84,
    "TT - Quill 85": TT_ID + QUILL_ID + 85,
    "TT - Quill 86": TT_ID + QUILL_ID + 86,
    "TT - Quill 87": TT_ID + QUILL_ID + 87,
    "TT - Quill 88": TT_ID + QUILL_ID + 88,
    "TT - Quill 89": TT_ID + QUILL_ID + 89,
    "TT - Quill 90": TT_ID + QUILL_ID + 90,
    "TT - Quill 91": TT_ID + QUILL_ID + 91,
    "TT - Quill 92": TT_ID + QUILL_ID + 92,
    "TT - Quill 93": TT_ID + QUILL_ID + 93,
    "TT - Quill 94": TT_ID + QUILL_ID + 94,
    "TT - Quill 95": TT_ID + QUILL_ID + 95,
    "TT - Quill 96": TT_ID + QUILL_ID + 96,
    "TT - Quill 97": TT_ID + QUILL_ID + 97,
    "TT - Quill 98": TT_ID + QUILL_ID + 98,
    "TT - Quill 99": TT_ID + QUILL_ID + 99,
    "TT - Quill 100": TT_ID + QUILL_ID + 100,
    "TT - Quill 101": TT_ID + QUILL_ID + 101,
    "TT - Quill 102": TT_ID + QUILL_ID + 102,
    "TT - Quill 103": TT_ID + QUILL_ID + 103,
    "TT - Quill 104": TT_ID + QUILL_ID + 104,
    "TT - Quill 105": TT_ID + QUILL_ID + 105,
    "TT - Quill 106": TT_ID + QUILL_ID + 106,
    "TT - Quill 107": TT_ID + QUILL_ID + 107,
    "TT - Quill 108": TT_ID + QUILL_ID + 108,
    "TT - Quill 109": TT_ID + QUILL_ID + 109,
    "TT - Quill 110": TT_ID + QUILL_ID + 110,
    "TT - Quill 111": TT_ID + QUILL_ID + 111,
    "TT - Quill 112": TT_ID + QUILL_ID + 112,
    "TT - Quill 113": TT_ID + QUILL_ID + 113,
    "TT - Quill 114": TT_ID + QUILL_ID + 114,
    "TT - Quill 115": TT_ID + QUILL_ID + 115,
    "TT - Quill 116": TT_ID + QUILL_ID + 116,
    "TT - Quill 117": TT_ID + QUILL_ID + 117,
    "TT - Quill 118": TT_ID + QUILL_ID + 118,
    "TT - Quill 119": TT_ID + QUILL_ID + 119,
    "TT - Quill 120": TT_ID + QUILL_ID + 120,
    "TT - Quill 121": TT_ID + QUILL_ID + 121,
    "TT - Quill 122": TT_ID + QUILL_ID + 122,
    "TT - Quill 123": TT_ID + QUILL_ID + 123,
    "TT - Quill 124": TT_ID + QUILL_ID + 124,
    "TT - Quill 125": TT_ID + QUILL_ID + 125,
    "TT - Quill 126": TT_ID + QUILL_ID + 126,
    "TT - Quill 127": TT_ID + QUILL_ID + 127,
    "TT - Quill 128": TT_ID + QUILL_ID + 128,
    "TT - Quill 129": TT_ID + QUILL_ID + 129,
    "TT - Quill 130": TT_ID + QUILL_ID + 130,
    "TT - Quill 131": TT_ID + QUILL_ID + 131,
    "TT - Quill 132": TT_ID + QUILL_ID + 132,
    "TT - Quill 133": TT_ID + QUILL_ID + 133,
    "TT - Quill 134": TT_ID + QUILL_ID + 134,
    "TT - Quill 135": TT_ID + QUILL_ID + 135,
    "TT - Quill 136": TT_ID + QUILL_ID + 136,
    "TT - Quill 137": TT_ID + QUILL_ID + 137,
    "TT - Quill 138": TT_ID + QUILL_ID + 138,
    "TT - Quill 139": TT_ID + QUILL_ID + 139,
    "TT - Quill 140": TT_ID + QUILL_ID + 140,
    "TT - Quill 141": TT_ID + QUILL_ID + 141,
    "TT - Quill 142": TT_ID + QUILL_ID + 142,
    "TT - Quill 143": TT_ID + QUILL_ID + 143,
    "TT - Quill 144": TT_ID + QUILL_ID + 144,
    "TT - Quill 145": TT_ID + QUILL_ID + 145,
    "TT - Quill 146": TT_ID + QUILL_ID + 146,
    "TT - Quill 147": TT_ID + QUILL_ID + 147,
    "TT - Quill 148": TT_ID + QUILL_ID + 148,
    "TT - Quill 149": TT_ID + QUILL_ID + 149,

    # # Tribalstack Tropics - Pagies
    "TT - Pagie 0": TT_ID + PAGIE_ID + 0,
    "TT - Pagie 1": TT_ID + PAGIE_ID + 1,
    "TT - Pagie 2": TT_ID + PAGIE_ID + 2,
    "TT - Pagie 3": TT_ID + PAGIE_ID + 3,
    "TT - Pagie 4": TT_ID + PAGIE_ID + 4,
    "TT - Pagie 5": TT_ID + PAGIE_ID + 5,
    "TT - Pagie 6": TT_ID + PAGIE_ID + 6,
    "TT - Pagie 7": TT_ID + PAGIE_ID + 7,
    "TT - Pagie 8": TT_ID + PAGIE_ID + 8,
    "TT - Pagie 9": TT_ID + PAGIE_ID + 9,
    "TT - Pagie 10": TT_ID + PAGIE_ID + 10,
    "TT - Pagie 11": TT_ID + PAGIE_ID + 11,
    "TT - Pagie 12": TT_ID + PAGIE_ID + 12,
    "TT - Pagie 13": TT_ID + PAGIE_ID + 13,
    "TT - Pagie 14": TT_ID + PAGIE_ID + 14,
    "TT - Pagie 15": TT_ID + PAGIE_ID + 15,
    "TT - Pagie 16": TT_ID + PAGIE_ID + 16,
    "TT - Pagie 17": TT_ID + PAGIE_ID + 17,
    "TT - Pagie 18": TT_ID + PAGIE_ID + 18,
    "TT - Pagie 19": TT_ID + PAGIE_ID + 19,
    "TT - Pagie 20": TT_ID + PAGIE_ID + 20,
    "TT - Pagie 21": TT_ID + PAGIE_ID + 21,
    "TT - Pagie 22": TT_ID + PAGIE_ID + 22,
    "TT - Pagie 23": TT_ID + PAGIE_ID + 23,
    "TT - Pagie 24": TT_ID + PAGIE_ID + 24,
    "TT - Pagie 25": TT_ID + PAGIE_ID + 25,
    "TT - Pagie 26": TT_ID + PAGIE_ID + 26,
    "TT - Pagie 27": TT_ID + PAGIE_ID + 27,
    "TT - Pagie 28": TT_ID + PAGIE_ID + 28,
    "TT - Pagie 29": TT_ID + PAGIE_ID + 29,
    "TT - Pagie 30": TT_ID + PAGIE_ID + 30,
    "TT - Pagie 31": TT_ID + PAGIE_ID + 31,
    "TT - Pagie 32": TT_ID + PAGIE_ID + 32,
    "TT - Pagie 33": TT_ID + PAGIE_ID + 33,
    "TT - Pagie 34": TT_ID + PAGIE_ID + 34,
    "TT - Pagie 35": TT_ID + PAGIE_ID + 35,
    "TT - Pagie 36": TT_ID + PAGIE_ID + 36,
    "TT - Pagie 37": TT_ID + PAGIE_ID + 37,
    "TT - Pagie 38": TT_ID + PAGIE_ID + 38,
    "TT - Pagie 39": TT_ID + PAGIE_ID + 39,
    "TT - Pagie 40": TT_ID + PAGIE_ID + 40,
    "TT - Pagie 41": TT_ID + PAGIE_ID + 41,
    "TT - Pagie 42": TT_ID + PAGIE_ID + 42,
    "TT - Pagie 43": TT_ID + PAGIE_ID + 43,
    "TT - Pagie 44": TT_ID + PAGIE_ID + 44,
    "TT - Pagie 45": TT_ID + PAGIE_ID + 45,
    "TT - Pagie 46": TT_ID + PAGIE_ID + 46,
    "TT - Pagie 47": TT_ID + PAGIE_ID + 47,
    "TT - Pagie 48": TT_ID + PAGIE_ID + 48,
    "TT - Pagie 49": TT_ID + PAGIE_ID + 49,
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
        [f"TT - Quill {i}" for i in range(150)]
    )
    tt_pagie_locations = get_location_names_with_ids(
        [f"TT - Pagie {i}" for i in range(50)]
    )
    tt_start_island.add_locations(tt_quill_locations, YookaReplayleeLocation)
    tt_start_island.add_locations(tt_pagie_locations, YookaReplayleeLocation)

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
