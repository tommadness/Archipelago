from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from Utils import visualize_regions

if TYPE_CHECKING:
    from .world import ReplayleeWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: ReplayleeWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: ReplayleeWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    ht_entrance = Region("Hivory Towers Entrance", world.player, world.multiworld)
    ht_near_tt = Region("Hivory Towers Near TT", world.player, world.multiworld)
    tt_start_island = Region("Tribalstack Tropics Starting Island", world.player, world.multiworld)
    tt_near_shovel_knight = Region("Tribalstack Tropics Near Shovel Knight", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [ht_entrance, ht_near_tt, tt_start_island, tt_near_shovel_knight]
    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: ReplayleeWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    ht_entrance = world.get_region("Hivory Towers Entrance")
    ht_near_tt = world.get_region("Hivory Towers Near TT")
    tt_start_island = world.get_region("Tribalstack Tropics Starting Island")
    tt_near_shovel_knight = world.get_region("Tribalstack Tropics Near Shovel Knight")

    # Okay, now we can get connecting. For this, we need to create Entrances.
    # Entrances are inherently one-way, but crucially, AP assumes you can always return to the origin region.
    # One way to create an Entrance is by calling the Entrance constructor.
    ht_entrance_to_ht_near_tt = Entrance(world.player, "Hivory Towers ramp to TT", parent=ht_entrance)
    ht_entrance.exits.append(ht_entrance_to_ht_near_tt)

    # You can then connect the Entrance to the target region.
    ht_entrance_to_ht_near_tt.connect(ht_near_tt)
    # An even easier way is to use the region.connect helper.
    ht_near_tt.connect(tt_start_island, "Hivory Towers to TT Start Island")
    tt_start_island.connect(tt_near_shovel_knight, "TT Start Island to Near Shovel Knight")


    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    # ht_near_tt.connect(tt_start_island, "Hivory Towers to TT Start Island", lambda state: state.has("Key", world.player))

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
"""     if world.options.hammer:
        top_middle_room = world.get_region("Top Middle Room")
        overworld.connect(top_middle_room, "Overworld to Top Middle Room") """
