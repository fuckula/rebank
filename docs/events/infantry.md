[← Events Index](../EVENTS.md) · [← Docs](../README.md)

# Infantry — sound events

Infantry ambient, foley, weapons, UAV and effects. **10 populated bank(s)** · **4056 named events**.

| Bank | Named events | Waveforms |
| --- | ---: | ---: |
| [`infantry_ambient`](#infantry_ambient) | 10 | 226 |
| [`infantry_effects`](#infantry_effects) | 352 | 1882 |
| [`infantry_explosions`](#infantry_explosions) | 84 | 382 |
| [`infantry_foley`](#infantry_foley) | 208 | 1733 |
| [`infantry_uav`](#infantry_uav) | 15 | 15 |
| [`infantry_vehicles`](#infantry_vehicles) | 13 | 67 |
| [`infantry_voices`](#infantry_voices) | 394 | 2267 |
| [`infantry_voices_narrator`](#infantry_voices_narrator) | 15 | 0 |
| [`infantry_weapon`](#infantry_weapon) | 279 | 5517 |
| [`infantry_weapon_foley`](#infantry_weapon_foley) | 2686 | 1839 |

## infantry_ambient

12 events (10 named), 226 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/aircraft/ambient/new_hangar/hangar_infantry` | nighttime, Event Orientation, prem, height, Distance |
| `event:/infantry/ambient/camera_underwater` |  |
| `event:/infantry/ambient/mc_city_battle` | distance, reverbIndoor, rain, daytime, surface, shooting, action, biome_grass, biome_forest |
| `event:/infantry/ambient/mc_city_middle_east` | distance, reverbIndoor, rain, surface, daytime, shooting, action, storm, biome_grass, biome_forest |
| `event:/infantry/ambient/mc_city_serpovo` | rain, distance, reverbIndoor, shooting, daytime, surface, action, biome_forest, biome_grass |
| `event:/infantry/ambient/mc_village_africa` | biome_grass, biome_forest, action, surface, daytime, shooting, distance, reverbIndoor, rain |
| `event:/infantry/ambient/mc_village_indochina` | shooting, daytime, surface, rain, distance, reverbIndoor, biome_forest, biome_grass, action |
| `event:/infantry/ambient/positioned/lake_mid` | soundSize, Distance |
| `event:/infantry/ambient/positioned/river_mid` | soundSize, Distance |
| `event:/infantry/ambient/rain` | mat, Elevation, reverbIndoor, model_type |

## infantry_effects

361 events (352 named), 1882 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/aircraft/gui/enemy_kill` |  |
| `event:/infantry/effects/ai/aphe_explosion` | Distance, occlusion |
| `event:/infantry/effects/ai/hit_aphe_big` | Distance, is_hit_ours, occlusion |
| `event:/infantry/effects/ai/hit_aphe_big_unpierce` | occlusion, is_hit_ours, Distance |
| `event:/infantry/effects/ai/hit_aphe_mid` | Distance, occlusion, is_hit_ours |
| `event:/infantry/effects/ai/hit_aphe_mid_unpierce` | Distance, occlusion, is_hit_ours |
| `event:/infantry/effects/ai/hit_aphe_small` | Distance, occlusion, is_hit_ours |
| `event:/infantry/effects/ai/hit_aphe_small_unpierce` | Distance, is_hit_ours, occlusion |
| `event:/infantry/effects/ai/hit_atgm` | occlusion, Distance, is_hit_ours |
| `event:/infantry/effects/ai/hit_atgm_unpierce` | occlusion, Distance, is_hit_ours |
| `event:/infantry/effects/ai/hit_big` | Distance, occlusion, is_hit_ours |
| `event:/infantry/effects/ai/hit_big_unpierce` | is_hit_ours, occlusion, Distance |
| `event:/infantry/effects/ai/hit_he_big` | Distance, occlusion, is_hit_ours |
| `event:/infantry/effects/ai/hit_he_big_unpierce` | Distance, occlusion, is_hit_ours |
| `event:/infantry/effects/ai/hit_he_mid` | Distance, is_hit_ours, occlusion |
| `event:/infantry/effects/ai/hit_he_mid_unpierce` | Distance, is_hit_ours, occlusion |
| `event:/infantry/effects/ai/hit_he_small` | Distance, occlusion, is_hit_ours |
| `event:/infantry/effects/ai/hit_he_small_unpierce` | occlusion, is_hit_ours, Distance |
| `event:/infantry/effects/ai/hit_heat_big` | occlusion, is_hit_ours, Distance |
| `event:/infantry/effects/ai/hit_heat_big_unpierce` | is_hit_ours, occlusion, Distance |
| `event:/infantry/effects/ai/hit_heat_mid` | Distance, is_hit_ours, occlusion |
| `event:/infantry/effects/ai/hit_heat_mid_unpierce` | Distance, is_hit_ours, occlusion |
| `event:/infantry/effects/ai/hit_heat_small` | is_hit_ours, occlusion, Distance |
| `event:/infantry/effects/ai/hit_heat_small_unpierce` | occlusion, is_hit_ours, Distance |
| `event:/infantry/effects/ai/hit_mgun` | occlusion, is_hit_ours, Distance |
| `event:/infantry/effects/ai/hit_mid` | is_hit_ours, occlusion, Distance |
| `event:/infantry/effects/ai/hit_mid_unpierce` | Distance, occlusion, is_hit_ours |
| `event:/infantry/effects/ai/hit_small` | Distance, is_hit_ours, occlusion |
| `event:/infantry/effects/ai/hit_small_unpierce` | is_hit_ours, occlusion, Distance |
| `event:/infantry/effects/ai/rico` | Distance, occlusion, is_hit_ours |
| `event:/infantry/effects/ai/rico_mgun` | occlusion, is_hit_ours, Distance |
| `event:/infantry/effects/ai/rico_mid` | Distance, occlusion, is_hit_ours |
| `event:/infantry/effects/ai/rico_small` | is_hit_ours, occlusion, Distance |
| `event:/infantry/effects/bomb_ground_hit` | Distance |
| `event:/infantry/effects/bombs_incoming` | Distance, Direction |
| `event:/infantry/effects/bullet_passby` | velocity, caliber, occlusion, Distance |
| `event:/infantry/effects/bullethit_building` | occlusion, Distance |
| `event:/infantry/effects/bullethit_car` | occlusion, Distance |
| `event:/infantry/effects/bullethit_car_glass` | occlusion, Distance |
| `event:/infantry/effects/bullethit_ceramic` | occlusion, Distance |
| `event:/infantry/effects/bullethit_ground` | occlusion, Distance |
| `event:/infantry/effects/bullethit_piano` | occlusion, Distance |
| `event:/infantry/effects/bullethit_plastic` | occlusion, Distance |
| `event:/infantry/effects/bullethit_stone` | occlusion, Distance |
| `event:/infantry/effects/bullethit_unit` | is_hit_ours, occlusion, Distance |
| `event:/infantry/effects/bullethit_water` | Distance, occlusion |
| `event:/infantry/effects/bullethit_wood` | Distance, occlusion |
| `event:/infantry/effects/collision_body` | intense, Distance |
| `event:/infantry/effects/collision_bushes` | intense, Distance |
| `event:/infantry/effects/collision_rocks` | Distance, intense |
| `event:/infantry/effects/collision_tank` | Distance, intense |
| `event:/infantry/effects/collision_tree` | intense, Distance |
| `event:/infantry/effects/flame_hit` | Distance, timer |
| `event:/infantry/effects/flame_spot` | Distance |
| `event:/infantry/effects/missile_sonic_boom` | Distance |
| `event:/infantry/effects/napalm_spot` | Distance |
| `event:/infantry/effects/rocket_passby` | distance |
| `event:/infantry/enemy/effects/drone` | speed, DistanceDroneSmall |
| `event:/infantry/enemy/effects/drone_launch` | occlusion |
| `event:/infantry/enemy/effects/parachute_box_landing` |  |
| `event:/infantry/enemy/effects/parachute_landing` |  |
| `event:/infantry/enemy/walker/ww2_soldier/hit/bolt_body` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/bullet_body` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/bullet_body_big` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/melee` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/melee_axe` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/melee_aztec_sword` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/melee_bat` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/melee_hands` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/melee_japan_club` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/melee_japan_katana` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/melee_japan_stick` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/melee_knife` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/melee_pipe` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/melee_viking_hammer_common` | armored |
| `event:/infantry/enemy/walker/ww2_soldier/hit/melee_viking_hammer_royal` | armored |
| `event:/infantry/env_effects/air_siren` |  |
| `event:/infantry/env_effects/asian_wind_flute` |  |
| `event:/infantry/env_effects/asian_wind_harp` |  |
| `event:/infantry/env_effects/bamboo_bells` |  |
| `event:/infantry/env_effects/bamboo_metal_bells` |  |
| `event:/infantry/env_effects/bomb_site/activate_action` |  |
| `event:/infantry/env_effects/bomb_site/deactivate_action` |  |
| `event:/infantry/env_effects/bomb_site/destroy` |  |
| `event:/infantry/env_effects/bomb_site_idle` |  |
| `event:/infantry/env_effects/building/destroy` |  |
| `event:/infantry/env_effects/building/destroy_action` |  |
| `event:/infantry/env_effects/clocks/clock_a` |  |
| `event:/infantry/env_effects/collision/fridge` | force |
| `event:/infantry/env_effects/doors/bunker/close` |  |
| `event:/infantry/env_effects/doors/bunker/open` |  |
| `event:/infantry/env_effects/doors/gate/close` |  |
| `event:/infantry/env_effects/doors/gate/open` |  |
| `event:/infantry/env_effects/doors/hatch/close` |  |
| `event:/infantry/env_effects/doors/hatch/open` |  |
| `event:/infantry/env_effects/doors/metal/breaking` |  |
| `event:/infantry/env_effects/doors/metal/closed` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal/locking` |  |
| `event:/infantry/env_effects/doors/metal/moving` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal/opened` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal/push` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal/stopped` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal_bunker/closed` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_bunker/moving` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal_bunker/opened` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal_bunker/push` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_bunker/stopped` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_fence/closed` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal_fence/moving` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_fence/opened` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_fence/push` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal_fence/stopped` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_gate/closed` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_gate/moving` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal_gate/opened` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal_gate/push` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal_gate/stopped` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_gate_01/close` |  |
| `event:/infantry/env_effects/doors/metal_gate_01/open` |  |
| `event:/infantry/env_effects/doors/metal_hatch/closed` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal_hatch/moving` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_hatch/opened` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal_hatch/push` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal_hatch/stopped` | velocity, occlusion |
| `event:/infantry/env_effects/doors/metal_locker/closed` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_locker/moving` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_locker/opened` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_locker/push` | occlusion, velocity |
| `event:/infantry/env_effects/doors/metal_locker/stopped` | occlusion, velocity |
| `event:/infantry/env_effects/doors/modern_metal_gate/close` |  |
| `event:/infantry/env_effects/doors/modern_metal_gate/open` |  |
| `event:/infantry/env_effects/doors/modern_wooden_gate/close` |  |
| `event:/infantry/env_effects/doors/modern_wooden_gate/open` |  |
| `event:/infantry/env_effects/doors/normandy_decor_gate/close` |  |
| `event:/infantry/env_effects/doors/normandy_decor_gate/open` |  |
| `event:/infantry/env_effects/doors/plastic/breaking` |  |
| `event:/infantry/env_effects/doors/plastic/close` |  |
| `event:/infantry/env_effects/doors/plastic/closed` | occlusion, velocity |
| `event:/infantry/env_effects/doors/plastic/locking` |  |
| `event:/infantry/env_effects/doors/plastic/moving` | occlusion, velocity |
| `event:/infantry/env_effects/doors/plastic/open` |  |
| `event:/infantry/env_effects/doors/plastic/opened` | velocity, occlusion |
| `event:/infantry/env_effects/doors/plastic/push` | occlusion, velocity |
| `event:/infantry/env_effects/doors/plastic/stopped` | occlusion, velocity |
| `event:/infantry/env_effects/doors/scary/close` |  |
| `event:/infantry/env_effects/doors/scary/open` |  |
| `event:/infantry/env_effects/doors/standart/close` |  |
| `event:/infantry/env_effects/doors/standart/open` |  |
| `event:/infantry/env_effects/doors/window/close` |  |
| `event:/infantry/env_effects/doors/window/open` |  |
| `event:/infantry/env_effects/doors/window_plastic/close` |  |
| `event:/infantry/env_effects/doors/window_plastic/closed` | occlusion, velocity |
| `event:/infantry/env_effects/doors/window_plastic/moving` | velocity, occlusion |
| `event:/infantry/env_effects/doors/window_plastic/open` |  |
| `event:/infantry/env_effects/doors/window_plastic/opened` | velocity, occlusion |
| `event:/infantry/env_effects/doors/window_plastic/push` | occlusion, velocity |
| `event:/infantry/env_effects/doors/window_plastic/stopped` | occlusion, velocity |
| `event:/infantry/env_effects/doors/wooden/breaking` |  |
| `event:/infantry/env_effects/doors/wooden/closed` | occlusion, velocity |
| `event:/infantry/env_effects/doors/wooden/locking` |  |
| `event:/infantry/env_effects/doors/wooden/moving` | occlusion, velocity |
| `event:/infantry/env_effects/doors/wooden/opened` | velocity, occlusion |
| `event:/infantry/env_effects/doors/wooden/push` | velocity, occlusion |
| `event:/infantry/env_effects/doors/wooden/stopped` | velocity, occlusion |
| `event:/infantry/env_effects/doors/wooden_window/closed` | velocity, occlusion |
| `event:/infantry/env_effects/doors/wooden_window/moving` | occlusion, velocity |
| `event:/infantry/env_effects/doors/wooden_window/opened` | occlusion, velocity |
| `event:/infantry/env_effects/doors/wooden_window/push` | velocity, occlusion |
| `event:/infantry/env_effects/doors/wooden_window/stopped` | occlusion, velocity |
| `event:/infantry/env_effects/drain_bright_a` |  |
| `event:/infantry/env_effects/drain_deep_a` |  |
| `event:/infantry/env_effects/electric_continious_sparks` |  |
| `event:/infantry/env_effects/electric_sparks` |  |
| `event:/infantry/env_effects/electrical_panel_a` |  |
| `event:/infantry/env_effects/electrical_panel_b` |  |
| `event:/infantry/env_effects/electrical_panel_c` |  |
| `event:/infantry/env_effects/explosive_installed` | explosive_timer, ExplosiveInstalledDistance |
| `event:/infantry/env_effects/fire/dirt_fire_crackle` |  |
| `event:/infantry/env_effects/fire/fire_character` |  |
| `event:/infantry/env_effects/fire/fire_mid` | occlusion |
| `event:/infantry/env_effects/fire/fire_molotov` |  |
| `event:/infantry/env_effects/fire/fire_small` |  |
| `event:/infantry/env_effects/fire/fire_vehicle` |  |
| `event:/infantry/env_effects/fire/grenade_smoke` |  |
| `event:/infantry/env_effects/fire/grenade_torch` |  |
| `event:/infantry/env_effects/fire/lava` |  |
| `event:/infantry/env_effects/fire/lava_splash` |  |
| `event:/infantry/env_effects/generator` |  |
| `event:/infantry/env_effects/lamp_hum` | brightness |
| `event:/infantry/env_effects/lamp_off` |  |
| `event:/infantry/env_effects/lamp_on` |  |
| `event:/infantry/env_effects/mc_explosive_installed` | ExplosiveInstalledDistance, occlusion, explosive_timer |
| `event:/infantry/env_effects/metal_gates_a` |  |
| `event:/infantry/env_effects/mill/mill_inside` | reverbIndoor |
| `event:/infantry/env_effects/mill/mill_outside` | reverbIndoor |
| `event:/infantry/env_effects/rally_point` |  |
| `event:/infantry/env_effects/steam/steam_stream` |  |
| `event:/infantry/env_effects/steam/steam_stream_small` |  |
| `event:/infantry/env_effects/transformator_a` |  |
| `event:/infantry/env_effects/transformator_b` |  |
| `event:/infantry/env_effects/transformator_c` |  |
| `event:/infantry/env_effects/ventilation_exhaust` |  |
| `event:/infantry/explosions/parts_explosion` | reverbIndoor, Direction, Distance, headphones, occlusion |
| `event:/infantry/impact/ampula_shell` | Distance |
| `event:/infantry/impact/artillery_rocket` | Distance, mat, cal |
| `event:/infantry/impact/artillery_smoke` | Distance, mat, cal |
| `event:/infantry/impact/aspen_stake` | mat |
| `event:/infantry/impact/axe` | mat |
| `event:/infantry/impact/aztec_sword` | mat |
| `event:/infantry/impact/barrage_baloon` | Distance |
| `event:/infantry/impact/bat` | mat |
| `event:/infantry/impact/bolt` | cal, mat, Distance |
| `event:/infantry/impact/bomb` | mat, cal, Distance |
| `event:/infantry/impact/bomb_explode` | mat, cal, Distance |
| `event:/infantry/impact/bomb_hit` | Distance, DistanceNoExplosion, cal, mat |
| `event:/infantry/impact/bomb_timer` | bomb_timer |
| `event:/infantry/impact/bullet` | Distance, cal, mat, friendlyBullet, suppress_bullet_snapshot |
| `event:/infantry/impact/burma_bell` | dmg, Distance |
| `event:/infantry/impact/car_explosion` | Distance |
| `event:/infantry/impact/church_bell` | dmg, Distance |
| `event:/infantry/impact/church_bell_fallen` | Distance, dmg, DistanceFallen |
| `event:/infantry/impact/crash_site_smoke` |  |
| `event:/infantry/impact/explode_ammo` | Distance |
| `event:/infantry/impact/flak_air` | Distance |
| `event:/infantry/impact/fly_artillery_rocket_projectile` | Distance |
| `event:/infantry/impact/fly_bomb_mid` |  |
| `event:/infantry/impact/fly_bomb_player` |  |
| `event:/infantry/impact/fly_javelin_projectile` | Distance |
| `event:/infantry/impact/fly_mine_projectile` | Distance |
| `event:/infantry/impact/fly_rocket_projectile` | Distance |
| `event:/infantry/impact/flyby` | Distance, cal, FlyByDistance |
| `event:/infantry/impact/fragment` | Distance, cal, mat |
| `event:/infantry/impact/gasoline` | Distance |
| `event:/infantry/impact/grenade` | Distance |
| `event:/infantry/impact/grenade_flash` | Distance |
| `event:/infantry/impact/hands` | mat |
| `event:/infantry/impact/incendiary_grenade` | Distance |
| `event:/infantry/impact/japan_club` | mat |
| `event:/infantry/impact/japan_katana` | mat |
| `event:/infantry/impact/japan_stick` | mat |
| `event:/infantry/impact/kamikaze_drone` | DistanceDroneBig, Distance |
| `event:/infantry/impact/knife` | mat |
| `event:/infantry/impact/knife_hit_dirt` | Distance, occlusion |
| `event:/infantry/impact/knife_hit_generic` | Distance, occlusion |
| `event:/infantry/impact/knife_hit_metal` | occlusion, Distance |
| `event:/infantry/impact/knife_hit_stone` | Distance, occlusion |
| `event:/infantry/impact/knife_hit_wood` | occlusion, Distance |
| `event:/infantry/impact/melee` | mat |
| `event:/infantry/impact/melee_piano` | Distance |
| `event:/infantry/impact/mine` | Event Cone Angle, Distance |
| `event:/infantry/impact/mine_activate` | Distance |
| `event:/infantry/impact/molotov` | Distance |
| `event:/infantry/impact/pipe` | mat |
| `event:/infantry/impact/pitchfork` | mat |
| `event:/infantry/impact/recon_drone` | Distance, DistanceDroneSmall |
| `event:/infantry/impact/rico_bullet` | cal, mat, Distance |
| `event:/infantry/impact/rocket` | cal, mat, Distance |
| `event:/infantry/impact/shell` | Distance, mat, cal |
| `event:/infantry/impact/shell_projectile` | Distance |
| `event:/infantry/impact/shovel` | mat |
| `event:/infantry/impact/smoke_grenade` | Distance, cal, mat |
| `event:/infantry/impact/tank_explosion` | Distance |
| `event:/infantry/impact/tank_explosion_enemy` | Distance |
| `event:/infantry/impact/terraform` |  |
| `event:/infantry/impact/vehicle_mine` | Distance |
| `event:/infantry/impact/viking_hammer_common` | mat |
| `event:/infantry/impact/viking_hammer_royal` | mat |
| `event:/infantry/impact/wiz` | Distance, cal, suppress_bullet_snapshot |
| `event:/infantry/impact/wiz_bolt` | suppress_bullet_snapshot, Distance, cal |
| `event:/infantry/impact/wiz_fragment` | cal, FragmentDistance, suppress_bullet_snapshot |
| `event:/infantry/impact/wiz_large_caliber` | suppress_bullet_snapshot, Distance |
| `event:/infantry/impact/wiz_shell` | Distance, suppress_bullet_snapshot |
| `event:/infantry/impact/wiz_subsonic_bullet` | Distance, suppress_bullet_snapshot |
| `event:/infantry/impact/wiz_supersonic_bullet` | suppress_bullet_snapshot, Distance |
| `event:/infantry/object_crash/bamboo_bells` |  |
| `event:/infantry/object_crash/bamboo_metal_bells` |  |
| `event:/infantry/object_crash/bollard` |  |
| `event:/infantry/object_crash/bollard_fall` |  |
| `event:/infantry/object_crash/building_big` | Distance |
| `event:/infantry/object_crash/building_creak` | Distance |
| `event:/infantry/object_crash/building_fall_big` | Distance |
| `event:/infantry/object_crash/building_fall_mid` | Distance |
| `event:/infantry/object_crash/building_fall_small` | Distance |
| `event:/infantry/object_crash/building_hit` | Distance |
| `event:/infantry/object_crash/cactus` |  |
| `event:/infantry/object_crash/car_wreck` |  |
| `event:/infantry/object_crash/ceramic` |  |
| `event:/infantry/object_crash/concrete_big` |  |
| `event:/infantry/object_crash/concrete_mid` |  |
| `event:/infantry/object_crash/concrete_mid_fall` |  |
| `event:/infantry/object_crash/glass` |  |
| `event:/infantry/object_crash/haystack` | Distance |
| `event:/infantry/object_crash/haystack_medium` |  |
| `event:/infantry/object_crash/hydrant` |  |
| `event:/infantry/object_crash/mannequin_down` |  |
| `event:/infantry/object_crash/mannequin_up` |  |
| `event:/infantry/object_crash/metal_door` |  |
| `event:/infantry/object_crash/metal_grid` |  |
| `event:/infantry/object_crash/metal_grid_fall` |  |
| `event:/infantry/object_crash/metal_mid` |  |
| `event:/infantry/object_crash/metal_mid_fall` |  |
| `event:/infantry/object_crash/metal_small` |  |
| `event:/infantry/object_crash/paper` | Distance |
| `event:/infantry/object_crash/plastic_door` |  |
| `event:/infantry/object_crash/projector` |  |
| `event:/infantry/object_crash/sandbag` |  |
| `event:/infantry/object_crash/tree` | tree_height, is_bush |
| `event:/infantry/object_crash/tree_fall` | tree_height, is_bush |
| `event:/infantry/object_crash/window` |  |
| `event:/infantry/object_crash/window_dmg` |  |
| `event:/infantry/object_crash/wood_big` |  |
| `event:/infantry/object_crash/wood_building_hit_big` | Distance |
| `event:/infantry/object_crash/wood_building_hit_mid` | Distance |
| `event:/infantry/object_crash/wood_building_hit_small` | Distance |
| `event:/infantry/object_crash/wood_dmg` |  |
| `event:/infantry/object_crash/wood_metal` |  |
| `event:/infantry/object_crash/wood_metal_big` |  |
| `event:/infantry/object_crash/wood_mid` |  |
| `event:/infantry/object_crash/wood_small` |  |
| `event:/infantry/object_crash/wooden_door` |  |
| `event:/infantry/player/effects/death_cam` | death_cam_saturation |
| `event:/infantry/player/effects/death_tinnitus` |  |
| `event:/infantry/player/effects/drone_in` |  |
| `event:/infantry/player/effects/drone_launch` |  |
| `event:/infantry/player/effects/drone_out` |  |
| `event:/infantry/player/effects/fall_wind` | altitude, speed |
| `event:/infantry/player/effects/parachute_flight` | altitude |
| `event:/infantry/player/effects/parachute_jump` |  |
| `event:/infantry/player/effects/parachute_landing` |  |
| `event:/infantry/player/effects/parachute_open` |  |
| `event:/infantry/player/effects/parachute_siren` |  |
| `event:/infantry/player/effects/tinnitus` | pow |
| `event:/infantry/player/walker/_common_foley/ammunition_mc_soldier/sprint` | mat |
| `event:/infantry/player/walker/mc_soldier/foley_mov/bodyfall` | depth, mat |
| `event:/infantry/player/walker/ww2_soldier/hit/bolt_body` | armored, suppress_bullet_snapshot |
| `event:/infantry/player/walker/ww2_soldier/hit/bullet_body` | suppress_bullet_snapshot, armored |
| `event:/infantry/player/walker/ww2_soldier/hit/bullet_body_big` | suppress_bullet_snapshot, armored |
| `event:/infantry/player/walker/ww2_soldier/hit/bullet_helmet` | suppress_bullet_snapshot, armored |
| `event:/infantry/player/walker/ww2_soldier/hit/melee` | armored |
| `event:/infantry/player/walker/ww2_soldier/hit/melee_axe` | armored |
| `event:/infantry/player/walker/ww2_soldier/hit/melee_aztec_sword` | armored |
| `event:/infantry/player/walker/ww2_soldier/hit/melee_bat` | armored |
| `event:/infantry/player/walker/ww2_soldier/hit/melee_hands` | armored |
| `event:/infantry/player/walker/ww2_soldier/hit/melee_japan_club` | armored |
| `event:/infantry/player/walker/ww2_soldier/hit/melee_japan_katana` | armored |
| `event:/infantry/player/walker/ww2_soldier/hit/melee_japan_stick` | armored |
| `event:/infantry/player/walker/ww2_soldier/hit/melee_knife` | armored |
| `event:/infantry/player/walker/ww2_soldier/hit/melee_pipe` | armored |
| `event:/infantry/player/walker/ww2_soldier/hit/melee_viking_hammer_common` | armored |
| `event:/infantry/player/walker/ww2_soldier/hit/melee_viking_hammer_royal` | armored |
| `event:/infantry/snapshots/reverb_indoor` | elongation, absorptionReverb, reverbIndoor, elongationReverb, isPlayerIndoor, roomSize, absorption, roomSizeReverb |
| `event:/infantry/ui/helmet_hit` |  |

## infantry_explosions

100 events (84 named), 382 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/infantry/effects/wreck_explosion` | Direction, reverbIndoor, occlusion, Distance, headphones |
| `event:/infantry/explosions/ammo_explode` | occlusion, timer, headphones, Distance, Direction, reverbIndoor |
| `event:/infantry/explosions/ammo_explode_crate` | Direction, reverbIndoor, timer, occlusion, headphones, Distance |
| `event:/infantry/explosions/art_explosion_concrete` | Direction, reverbIndoor, timer, occlusion, headphones, Distance |
| `event:/infantry/explosions/art_explosion_ground` | reverbIndoor, Direction, Distance, headphones, occlusion, timer |
| `event:/infantry/explosions/art_explosion_metal` | reverbIndoor, Direction, headphones, Distance, timer, occlusion |
| `event:/infantry/explosions/art_explosion_water` | Distance, headphones, occlusion, timer, reverbIndoor, Direction |
| `event:/infantry/explosions/art_explosion_wood` | occlusion, timer, headphones, Distance, Direction, reverbIndoor |
| `event:/infantry/explosions/art_heavy_concrete` | Direction, reverbIndoor, occlusion, timer, Distance, headphones |
| `event:/infantry/explosions/art_heavy_ground` | reverbIndoor, Direction, headphones, Distance, occlusion, timer |
| `event:/infantry/explosions/art_heavy_metal` | headphones, Distance, occlusion, timer, reverbIndoor, Direction |
| `event:/infantry/explosions/art_heavy_water` | timer, occlusion, headphones, Distance, Direction, reverbIndoor |
| `event:/infantry/explosions/art_heavy_wood` | reverbIndoor, Direction, Distance, headphones, timer, occlusion |
| `event:/infantry/explosions/art_no_expl_concrete` | occlusion, timer, Distance, headphones, Direction, reverbIndoor |
| `event:/infantry/explosions/art_no_expl_ground` | reverbIndoor, Direction, Distance, headphones, occlusion, timer |
| `event:/infantry/explosions/art_no_expl_metal` | reverbIndoor, Direction, headphones, Distance, occlusion, timer |
| `event:/infantry/explosions/art_no_expl_water` | Direction, reverbIndoor, timer, occlusion, Distance, headphones |
| `event:/infantry/explosions/art_no_expl_wood` | Direction, reverbIndoor, timer, occlusion, headphones, Distance |
| `event:/infantry/explosions/art_preparation_concrete` | timer, occlusion, headphones, Distance, Direction, on_shot, is_marker, reverbIndoor |
| `event:/infantry/explosions/art_preparation_ground` | timer, occlusion, Distance, headphones, Direction, is_marker, reverbIndoor, on_shot |
| `event:/infantry/explosions/art_preparation_metal` | occlusion, timer, headphones, Distance, Direction, is_marker, reverbIndoor, on_shot |
| `event:/infantry/explosions/art_preparation_water` | Direction, is_marker, reverbIndoor, on_shot, occlusion, timer, headphones, Distance |
| `event:/infantry/explosions/art_preparation_wood` | timer, occlusion, headphones, Distance, Direction, on_shot, is_marker, reverbIndoor |
| `event:/infantry/explosions/bomb_expl_water_mid` | occlusion, Distance, headphones, Direction, reverbIndoor |
| `event:/infantry/explosions/bomb_expl_water_small` | reverbIndoor, Direction, headphones, Distance, occlusion |
| `event:/infantry/explosions/bomb_explosion_ground` | occlusion, Distance, headphones, Direction, reverbIndoor |
| `event:/infantry/explosions/bomb_explosion_mid` | occlusion, headphones, Distance, Direction, reverbIndoor |
| `event:/infantry/explosions/bomb_explosion_small` | Distance, headphones, occlusion, reverbIndoor, Direction |
| `event:/infantry/explosions/bomb_explosion_water` | Distance, headphones, occlusion, reverbIndoor, Direction |
| `event:/infantry/explosions/bridge_crush` | Direction, reverbIndoor, timer, occlusion, headphones, Distance |
| `event:/infantry/explosions/destroy` | Distance, headphones, occlusion, timer, reverbIndoor, Direction |
| `event:/infantry/explosions/engine_burn` | occlusion, Distance, headphones, Direction, reverbIndoor |
| `event:/infantry/explosions/expl_building_heavy` | headphones, Distance, timer, occlusion, reverbIndoor, Direction |
| `event:/infantry/explosions/expl_building_med` | Direction, reverbIndoor, timer, occlusion, Distance, headphones |
| `event:/infantry/explosions/expl_oil_heavy` | Distance, headphones, timer, occlusion, reverbIndoor, Direction |
| `event:/infantry/explosions/explosion_air` | reverbIndoor, Direction, Distance, headphones, occlusion, timer |
| `event:/infantry/explosions/explosion_air_small` | Direction, reverbIndoor, occlusion, timer, Distance, headphones |
| `event:/infantry/explosions/explosion_building` | timer, occlusion, Distance, headphones, Direction, reverbIndoor |
| `event:/infantry/explosions/explosion_concrete` | headphones, Distance, timer, occlusion, reverbIndoor, Direction |
| `event:/infantry/explosions/explosion_gr_smoke` | Direction, reverbIndoor, occlusion, Distance, headphones |
| `event:/infantry/explosions/explosion_grenade` | occlusion, timer, Distance, headphones, Direction, reverbIndoor |
| `event:/infantry/explosions/explosion_ground` | Distance, headphones, timer, occlusion, reverbIndoor, Direction |
| `event:/infantry/explosions/explosion_ground_20_37` | Direction, reverbIndoor, occlusion, timer, Distance, headphones |
| `event:/infantry/explosions/explosion_ground_37_50` | reverbIndoor, Direction, Distance, headphones, timer, occlusion |
| `event:/infantry/explosions/explosion_ground_rapid` | occlusion, timer, headphones, Distance, Direction, reverbIndoor |
| `event:/infantry/explosions/explosion_metal` | timer, occlusion, headphones, Distance, Direction, reverbIndoor |
| `event:/infantry/explosions/explosion_metal_rapid` | headphones, Distance, occlusion, timer, reverbIndoor, Direction |
| `event:/infantry/explosions/explosion_metal_small` | Direction, reverbIndoor, timer, occlusion, Distance, headphones |
| `event:/infantry/explosions/explosion_naval` | headphones, Distance, occlusion, timer, reverbIndoor, Direction |
| `event:/infantry/explosions/explosion_stone_rapid` | reverbIndoor, Direction, headphones, Distance, timer, occlusion |
| `event:/infantry/explosions/explosion_stone_small` | headphones, Distance, timer, occlusion, reverbIndoor, Direction |
| `event:/infantry/explosions/explosion_unit` | Distance, headphones, occlusion, timer, reverbIndoor, Direction |
| `event:/infantry/explosions/explosion_water` | Direction, reverbIndoor, occlusion, timer, Distance, headphones |
| `event:/infantry/explosions/explosion_water_rapid` | Direction, reverbIndoor, timer, occlusion, headphones, Distance |
| `event:/infantry/explosions/explosion_water_small` | Direction, reverbIndoor, timer, occlusion, Distance, headphones |
| `event:/infantry/explosions/explosion_wood` | Direction, reverbIndoor, timer, occlusion, Distance, headphones |
| `event:/infantry/explosions/explosion_wood_rapid` | Direction, reverbIndoor, timer, occlusion, headphones, Distance |
| `event:/infantry/explosions/fire_building` | headphones, Distance, occlusion, Direction |
| `event:/infantry/explosions/fire_destroyed` | Distance, headphones, occlusion, Direction |
| `event:/infantry/explosions/fire_destroyed_big` | Distance, Direction, headphones, occlusion |
| `event:/infantry/explosions/ground_splash` | Direction, reverbIndoor, occlusion, Distance, headphones |
| `event:/infantry/explosions/heavy_explosion_air` | headphones, Distance, timer, occlusion, reverbIndoor, Direction |
| `event:/infantry/explosions/heavy_explosion_building` | Direction, reverbIndoor, timer, headphones, Distance |
| `event:/infantry/explosions/heavy_explosion_ground` | timer, Distance, headphones, Direction, reverbIndoor |
| `event:/infantry/explosions/heavy_explosion_unit` | Distance, headphones, timer, reverbIndoor, Direction |
| `event:/infantry/explosions/heavy_explosion_water` | Direction, reverbIndoor, timer, Distance, headphones |
| `event:/infantry/explosions/misl_explosion_ground` | occlusion, timer, headphones, Distance, Direction, reverbIndoor |
| `event:/infantry/explosions/misl_explosion_mid` | Direction, reverbIndoor, occlusion, timer, headphones, Distance |
| `event:/infantry/explosions/misl_explosion_small` | reverbIndoor, Direction, headphones, Distance, timer, occlusion |
| `event:/infantry/explosions/napaml_explosion` | reverbIndoor, Direction, headphones, Distance, occlusion, timer |
| `event:/infantry/explosions/napaml_stream` | reverbIndoor, Direction, headphones, Distance, occlusion, timer |
| `event:/infantry/explosions/no_explosive_concrete` | reverbIndoor, Direction, headphones, Distance, timer, occlusion |
| `event:/infantry/explosions/no_explosive_ground` | timer, occlusion, headphones, Distance, Direction, reverbIndoor |
| `event:/infantry/explosions/no_explosive_metal` | reverbIndoor, Direction, headphones, Distance, timer, occlusion |
| `event:/infantry/explosions/no_explosive_water` | reverbIndoor, Direction, Distance, headphones, timer, occlusion |
| `event:/infantry/explosions/no_explosive_wood` | timer, occlusion, headphones, Distance, Direction, reverbIndoor |
| `event:/infantry/explosions/parts_explosion_cockpit` | occlusion, headphones, Distance, Direction, reverbIndoor |
| `event:/infantry/explosions/plane_explosion_water` | occlusion, Distance, headphones, Direction, reverbIndoor |
| `event:/infantry/explosions/plane_explosion_water_cockpit` | Distance, headphones, occlusion, reverbIndoor, Direction |
| `event:/infantry/explosions/splash_metal` | Distance, headphones, occlusion, reverbIndoor, Direction |
| `event:/infantry/explosions/splash_wood` | reverbIndoor, Direction, headphones, Distance, occlusion |
| `event:/infantry/explosions/torpedo_explosion_unit` | Direction, reverbIndoor, occlusion, timer, Distance, headphones |
| `event:/infantry/explosions/wreck_explosion` | reverbIndoor, Direction, Distance, headphones, occlusion |
| `event:/infantry/explosions/wreck_uav` | Distance, headphones, occlusion, reverbIndoor, Direction |

## infantry_foley

208 events (208 named), 1733 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/infantry/ally/walker/mc_soldier/foley_mov/crawl_grains` | Distance, Elevation, depth, mat, EnemyStepDirection, occlusion, on_shot, headphones, Direction, SpeedRelative, isPlayerIndoor |
| `event:/infantry/ally/walker/mc_soldier/foley_mov/run_grains` | Direction, SpeedRelative, isPlayerIndoor, reverbIndoor, on_shot, headphones, Elevation, Distance, depth, mat, occlusion, EnemyStepDirection |
| `event:/infantry/ally/walker/mc_soldier/foley_mov/sprint_grains` | on_shot, headphones, Distance, Elevation, depth, mat, occlusion, EnemyStepDirection, Direction, SpeedRelative, isPlayerIndoor, reverbIndoor |
| `event:/infantry/ally/walker/mc_soldier/foley_mov/step_grains` | reverbIndoor, SpeedRelative, isPlayerIndoor, Direction, occlusion, EnemyStepDirection, depth, Elevation, Distance, mat, on_shot, headphones |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/bodyfall` | Distance, headphones, occlusion, Elevation, mat, reverbIndoor |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/common/climb` | isPlayerIndoor, Direction, headphones, EnemyStepDirection, occlusion, Distance, Elevation |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/common/climb_stair` | headphones, EnemyStepDirection, occlusion, Distance, Elevation, isPlayerIndoor, Direction |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/crawl_grains` | on_shot, headphones, depth, Distance, Elevation, mat, occlusion, EnemyStepDirection, Direction, SpeedRelative, isPlayerIndoor |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/down_ground` | headphones, EnemyStepDirection, occlusion, mat, Elevation, Distance, depth, isPlayerIndoor, Direction |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/down_knee` | headphones, mat, Distance, Elevation, EnemyStepDirection, occlusion, Direction, isPlayerIndoor |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/items/assembly/barrier_set` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/items/assembly/explosive_set` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/items/supplies/crate_ammo_pickup` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/items/supplies/crate_explosives_pickup` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/items/supplies/crate_heal_drop` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/items/supplies/crate_heal_pickup` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/jump_landing` | reverbIndoor, Direction, isPlayerIndoor, mat, depth, Elevation, Distance, EnemyStepDirection, occlusion, headphones |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/jump_start` | EnemyStepDirection, occlusion, depth, Distance, Elevation, mat, headphones, reverbIndoor, isPlayerIndoor, Direction |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/run_grains` | reverbIndoor, SpeedRelative, isPlayerIndoor, Direction, occlusion, EnemyStepDirection, Elevation, Distance, depth, mat, on_shot, headphones |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/sprint_grains` | on_shot, headphones, depth, Distance, Elevation, mat, occlusion, EnemyStepDirection, Direction, SpeedRelative, isPlayerIndoor, reverbIndoor |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/step_grains` | Direction, SpeedRelative, isPlayerIndoor, reverbIndoor, on_shot, headphones, Elevation, Distance, depth, mat, EnemyStepDirection, occlusion |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/swim/hand` | isPlayerIndoor, Direction, occlusion, Distance, Elevation, headphones |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/swim/leg` | isPlayerIndoor, Direction, headphones, occlusion, Distance, Elevation |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/up_ground` | occlusion, EnemyStepDirection, mat, Elevation, Distance, depth, headphones, isPlayerIndoor, Direction |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/up_knee` | Direction, isPlayerIndoor, headphones, mat, Elevation, Distance, occlusion, EnemyStepDirection |
| `event:/infantry/enemy/walker/ww2_soldier/collision/bush` | force |
| `event:/infantry/enemy/walker/ww2_soldier/collision/fall` | force |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/common/climb` |  |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/common/climb_stair` |  |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/common/mortair/aim_off` |  |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/common/mortair/aim_on` |  |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/crawl` | depth, mat |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/down_ground` | depth, mat |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/down_knee` | mat |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/jump_landing` | depth, mat |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/jump_start` | depth, mat |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/run` | depth, mat |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/sprint` | mat, depth |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/step` | depth, mat |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/swim/hand` |  |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/swim/leg` |  |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/up_ground` | depth, mat |
| `event:/infantry/enemy/walker/ww2_soldier/foley_mov/up_knee` | mat |
| `event:/infantry/enemy/walker/ww2_soldier/items/ammo/pick` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/armor/pick` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/build_cannon/activate` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/build_cannon/use` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/build_fortification/activate` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/build_fortification/use` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/flask/activate` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/flask/pick` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/grenade/pick` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/gun/pick` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/healing/activate` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/healing/pick` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/healing/use` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/other/pick` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/repairKit/use` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/revive/activate` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/revive/use` |  |
| `event:/infantry/enemy/walker/ww2_soldier/items/spray/activate` |  |
| `event:/infantry/player/walker/_common_foley/ammunition_mc_soldier/crawl` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_mc_soldier/down_ground` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_mc_soldier/down_knee` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_mc_soldier/jump_landing` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_mc_soldier/jump_start` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_mc_soldier/light` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_mc_soldier/run` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_mc_soldier/sprint` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_mc_soldier/up_ground` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_mc_soldier/up_knee` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_pan_armor/crawl` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_pan_armor/down_ground` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_pan_armor/down_knee` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_pan_armor/jump_landing` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_pan_armor/jump_start` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_pan_armor/run` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_pan_armor/sprint` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_pan_armor/step` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_pan_armor/up_ground` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_pan_armor/up_knee` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_ww2_soldier/crawl` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_ww2_soldier/down_ground` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_ww2_soldier/down_knee` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_ww2_soldier/jump_landing` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_ww2_soldier/jump_start` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_ww2_soldier/run` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_ww2_soldier/sprint` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_ww2_soldier/step` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_ww2_soldier/up_ground` | mat |
| `event:/infantry/player/walker/_common_foley/ammunition_ww2_soldier/up_knee` | mat |
| `event:/infantry/player/walker/_common_foley/cloth_mc_soldier/crawl` | mat |
| `event:/infantry/player/walker/_common_foley/cloth_ww2_soldier/crawl` | mat |
| `event:/infantry/player/walker/_common_foley/step_manequin/jump_landing` | mat |
| `event:/infantry/player/walker/_common_foley/step_manequin/jump_start` | mat |
| `event:/infantry/player/walker/_common_foley/step_manequin/run` | mat |
| `event:/infantry/player/walker/_common_foley/step_manequin/sprint` | mat |
| `event:/infantry/player/walker/_common_foley/step_manequin/step` | mat |
| `event:/infantry/player/walker/_common_foley/step_mc_soldier/jump_landing` | mat |
| `event:/infantry/player/walker/_common_foley/step_mc_soldier/jump_landing_interior` | mat |
| `event:/infantry/player/walker/_common_foley/step_mc_soldier/jump_start` | mat |
| `event:/infantry/player/walker/_common_foley/step_mc_soldier/jump_start_interior` | mat |
| `event:/infantry/player/walker/_common_foley/step_mc_soldier/run` | mat |
| `event:/infantry/player/walker/_common_foley/step_mc_soldier/run_interior` | mat |
| `event:/infantry/player/walker/_common_foley/step_mc_soldier/sprint` | mat |
| `event:/infantry/player/walker/_common_foley/step_mc_soldier/sprint_interior` | mat |
| `event:/infantry/player/walker/_common_foley/step_mc_soldier/step` | mat |
| `event:/infantry/player/walker/_common_foley/step_mc_soldier/step_interior` | mat |
| `event:/infantry/player/walker/_common_foley/step_naked/jump_landing` | mat |
| `event:/infantry/player/walker/_common_foley/step_naked/jump_start` | mat |
| `event:/infantry/player/walker/_common_foley/step_naked/run` | mat |
| `event:/infantry/player/walker/_common_foley/step_naked/sprint` | mat |
| `event:/infantry/player/walker/_common_foley/step_naked/step` | mat |
| `event:/infantry/player/walker/_common_foley/step_ww2_soldier/jump_landing` | mat |
| `event:/infantry/player/walker/_common_foley/step_ww2_soldier/jump_landing_interior` | mat |
| `event:/infantry/player/walker/_common_foley/step_ww2_soldier/jump_start` | mat |
| `event:/infantry/player/walker/_common_foley/step_ww2_soldier/jump_start_interior` | mat |
| `event:/infantry/player/walker/_common_foley/step_ww2_soldier/run` | mat |
| `event:/infantry/player/walker/_common_foley/step_ww2_soldier/run_interior` | mat |
| `event:/infantry/player/walker/_common_foley/step_ww2_soldier/sprint` | mat |
| `event:/infantry/player/walker/_common_foley/step_ww2_soldier/sprint_interior` | mat |
| `event:/infantry/player/walker/_common_foley/step_ww2_soldier/step` | mat |
| `event:/infantry/player/walker/_common_foley/step_ww2_soldier/step_interior` | mat |
| `event:/infantry/player/walker/mc_soldier/foley_mov/bodyfall` | depth, mat |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/antivehicle/aim_off` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/antivehicle/aim_on` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/climb` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/climb_stair` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/knife/close` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/knife/open` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/mgun/aim_off` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/mgun/aim_on` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/mortair/aim_off` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/mortair/aim_on` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/pistol/aim_off` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/pistol/aim_on` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/riffle/aim_off` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/riffle/aim_on` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/wpn_change_end` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/common/wpn_change_start` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/crawl_grains` | depth, mat, on_shot |
| `event:/infantry/player/walker/mc_soldier/foley_mov/down_ground` | mat, depth |
| `event:/infantry/player/walker/mc_soldier/foley_mov/down_knee` | mat, depth |
| `event:/infantry/player/walker/mc_soldier/foley_mov/items/assembly/barrier_set` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/items/assembly/explosive_set` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/items/supplies/crate_ammo_pickup` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/items/supplies/crate_explosives_pickup` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/items/supplies/crate_heal_drop` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/items/supplies/crate_heal_pickup` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/jump_landing` | reverbIndoor, mat, depth |
| `event:/infantry/player/walker/mc_soldier/foley_mov/jump_start` | reverbIndoor, depth, mat |
| `event:/infantry/player/walker/mc_soldier/foley_mov/run_grains` | reverbIndoor, depth, mat, on_shot |
| `event:/infantry/player/walker/mc_soldier/foley_mov/sprint_grains` | reverbIndoor, on_shot, on_step, depth, mat |
| `event:/infantry/player/walker/mc_soldier/foley_mov/step_grains` | reverbIndoor, mat, depth, on_shot |
| `event:/infantry/player/walker/mc_soldier/foley_mov/swim/hand` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/swim/leg` |  |
| `event:/infantry/player/walker/mc_soldier/foley_mov/up_ground` | depth, mat |
| `event:/infantry/player/walker/mc_soldier/foley_mov/up_knee` | mat, depth |
| `event:/infantry/player/walker/ww2_soldier/collision/bush` | force |
| `event:/infantry/player/walker/ww2_soldier/collision/fall` | force, armored |
| `event:/infantry/player/walker/ww2_soldier/collision/generic` | armored, force |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/antivehicle/aim_off` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/antivehicle/aim_on` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/climb` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/climb_stair` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/mgun/aim_off` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/mgun/aim_on` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/mortair/aim_off` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/mortair/aim_on` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/pistol/aim_off` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/pistol/aim_on` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/riffle/aim_off` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/riffle/aim_on` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/wpn_change_end` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/common/wpn_change_start` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/crawl` | depth, mat |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/down_ground` | mat, depth |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/down_knee` | depth, mat |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/jump_landing` | depth, mat |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/jump_start` | mat, depth |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/run` | mat, depth |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/sprint` | mat, depth |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/step` | mat, depth |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/swim/hand` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/swim/leg` |  |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/up_ground` | mat, depth |
| `event:/infantry/player/walker/ww2_soldier/foley_mov/up_knee` | depth, mat |
| `event:/infantry/player/walker/ww2_soldier/items/ammo/pick` |  |
| `event:/infantry/player/walker/ww2_soldier/items/armor/pick` |  |
| `event:/infantry/player/walker/ww2_soldier/items/build_cannon/activate` |  |
| `event:/infantry/player/walker/ww2_soldier/items/build_cannon/use` |  |
| `event:/infantry/player/walker/ww2_soldier/items/build_fortification/activate` |  |
| `event:/infantry/player/walker/ww2_soldier/items/build_fortification/use` |  |
| `event:/infantry/player/walker/ww2_soldier/items/fire_extinguish/activate` |  |
| `event:/infantry/player/walker/ww2_soldier/items/flask/activate` |  |
| `event:/infantry/player/walker/ww2_soldier/items/flask/pick` |  |
| `event:/infantry/player/walker/ww2_soldier/items/grenade/drop` | Distance |
| `event:/infantry/player/walker/ww2_soldier/items/grenade/pick` |  |
| `event:/infantry/player/walker/ww2_soldier/items/gun/pick` |  |
| `event:/infantry/player/walker/ww2_soldier/items/healing/activate` |  |
| `event:/infantry/player/walker/ww2_soldier/items/healing/pick` |  |
| `event:/infantry/player/walker/ww2_soldier/items/healing/use` |  |
| `event:/infantry/player/walker/ww2_soldier/items/loot_box/activate` |  |
| `event:/infantry/player/walker/ww2_soldier/items/other/drop` |  |
| `event:/infantry/player/walker/ww2_soldier/items/other/pick` |  |
| `event:/infantry/player/walker/ww2_soldier/items/repairKit/use` |  |
| `event:/infantry/player/walker/ww2_soldier/items/revive/activate` |  |
| `event:/infantry/player/walker/ww2_soldier/items/revive/use` |  |

## infantry_uav

16 events (15 named), 15 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/infantry/uav/engines/engine_uav_fpv_strike` | depth, event_vertical_angle, Distance, rpm, overload, load, Event Cone Angle, zoom |
| `event:/infantry/uav/engines/engine_uav_fpv_strike_ai` | Direction, overload, is_enemy, is_visible, rpm, headphones, Elevation, Event Cone Angle, occlusion, load, Distance |
| `event:/infantry/uav/engines/engine_uav_fpv_strike_prop` | Distance |
| `event:/infantry/uav/engines/engine_uav_fpv_strike_start` | Distance |
| `event:/infantry/uav/engines/engine_uav_fpv_strike_stop` | Distance |
| `event:/infantry/uav/engines/engine_uav_recon` | Event Cone Angle, load, zoom, rpm, Distance, event_vertical_angle, depth, overload |
| `event:/infantry/uav/engines/engine_uav_recon_ai` | headphones, load, occlusion, Distance, Event Cone Angle, Elevation, is_enemy, Direction, overload, is_visible, rpm |
| `event:/infantry/uav/engines/engine_uav_recon_prop` | Distance |
| `event:/infantry/uav/engines/engine_uav_recon_start` | Distance |
| `event:/infantry/uav/engines/engine_uav_recon_stop` | Distance |
| `event:/infantry/uav/engines/engine_uav_strike` | overload, Distance, rpm, depth, event_vertical_angle, zoom, Event Cone Angle, load |
| `event:/infantry/uav/engines/engine_uav_strike_ai` | overload, Direction, is_enemy, rpm, is_visible, headphones, Elevation, Event Cone Angle, Distance, load, occlusion |
| `event:/infantry/uav/engines/engine_uav_strike_prop` | Distance |
| `event:/infantry/uav/engines/engine_uav_strike_start` | Distance |
| `event:/infantry/uav/engines/engine_uav_strike_stop` | Distance |

## infantry_vehicles

14 events (13 named), 67 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/ground/effects/engine_cooldown` |  |
| `event:/ground/engines/ai/_enemies/humvee/engine` | occlusion, Distance, headphones, swim, load, is_visible, building_density, broken, Direction, rpm, loadswitch |
| `event:/ground/engines/ai/_enemies/humvee/engine_start` | is_visible, Direction, Distance, occlusion, headphones |
| `event:/ground/engines/ai/_enemies/humvee/engine_stop` | is_visible, Direction, Distance, occlusion, headphones |
| `event:/ground/engines/ai/humvee/engine` | swim, headphones, Distance, occlusion, loadswitch, rpm, Direction, broken, building_density, is_visible, load |
| `event:/ground/engines/ai/humvee/engine_start` | occlusion, Distance, headphones, is_visible, Direction |
| `event:/ground/engines/ai/humvee/engine_stop` | is_visible, Direction, occlusion, Distance, headphones |
| `event:/ground/engines/humvee/engine` | Event Cone Angle, volume_ducking, rpm, speed, loadswitch, broken, rpm_result_2c25, climb, Distance, load |
| `event:/ground/engines/humvee/engine_interior` | loadswitch, rpm, speed, rpm_result_2c25, broken, load, Distance |
| `event:/ground/engines/humvee/engine_start` | climb, Distance |
| `event:/ground/engines/humvee/engine_start_interior` | Distance |
| `event:/ground/engines/humvee/engine_stop` | Distance, climb |
| `event:/ground/engines/humvee/engine_stop_interior` | Distance |

## infantry_voices

912 events (394 named), 2267 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/bodyfall` | Distance, headphones, occlusion, Elevation, mat, reverbIndoor |
| `event:/infantry/enemy/walker/mc_soldier/voice_fx/bodyfall` | Distance, occlusion |
| `event:/infantry/enemy/walker/mc_soldier/voice_fx/burning` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier/voice_fx/cough` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier/voice_fx/death` | occlusion, Distance, reverbIndoor |
| `event:/infantry/enemy/walker/mc_soldier/voice_fx/downed` | occlusion, reverbIndoor |
| `event:/infantry/enemy/walker/mc_soldier/voice_fx/fall` | reverbIndoor, occlusion |
| `event:/infantry/enemy/walker/mc_soldier/voice_fx/hit` | occlusion, reverbIndoor |
| `event:/infantry/enemy/walker/mc_soldier/voice_fx/melee` | reverbIndoor, Distance, occlusion |
| `event:/infantry/enemy/walker/mc_soldier01/voice_fx/bodyfall` | occlusion, Distance |
| `event:/infantry/enemy/walker/mc_soldier01/voice_fx/burning` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier01/voice_fx/cough` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier01/voice_fx/death` | reverbIndoor, occlusion, Distance |
| `event:/infantry/enemy/walker/mc_soldier01/voice_fx/downed` | reverbIndoor, occlusion |
| `event:/infantry/enemy/walker/mc_soldier01/voice_fx/fall` | occlusion, reverbIndoor |
| `event:/infantry/enemy/walker/mc_soldier01/voice_fx/hit` | occlusion, reverbIndoor |
| `event:/infantry/enemy/walker/mc_soldier01/voice_fx/melee` | Distance, occlusion, reverbIndoor |
| `event:/infantry/enemy/walker/mc_soldier02/voice_fx/bodyfall` | occlusion, Distance |
| `event:/infantry/enemy/walker/mc_soldier02/voice_fx/burning` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier02/voice_fx/cough` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier02/voice_fx/death` | reverbIndoor, occlusion, Distance |
| `event:/infantry/enemy/walker/mc_soldier02/voice_fx/downed` | occlusion, reverbIndoor |
| `event:/infantry/enemy/walker/mc_soldier02/voice_fx/fall` | occlusion, reverbIndoor |
| `event:/infantry/enemy/walker/mc_soldier02/voice_fx/hit` | reverbIndoor, occlusion |
| `event:/infantry/enemy/walker/mc_soldier02/voice_fx/melee` | reverbIndoor, Distance, occlusion |
| `event:/infantry/enemy/walker/mc_soldier03/voice_fx/bodyfall` | Distance, occlusion |
| `event:/infantry/enemy/walker/mc_soldier03/voice_fx/burning` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier03/voice_fx/cough` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier03/voice_fx/death` | reverbIndoor, occlusion, Distance |
| `event:/infantry/enemy/walker/mc_soldier03/voice_fx/downed` | reverbIndoor, occlusion |
| `event:/infantry/enemy/walker/mc_soldier03/voice_fx/fall` | reverbIndoor, occlusion |
| `event:/infantry/enemy/walker/mc_soldier03/voice_fx/hit` | occlusion, reverbIndoor |
| `event:/infantry/enemy/walker/mc_soldier03/voice_fx/melee` | reverbIndoor, occlusion, Distance |
| `event:/infantry/enemy/walker/ww2_female_soldier/voice_fx/bodyfall` | Distance |
| `event:/infantry/enemy/walker/ww2_female_soldier/voice_fx/burning` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier/voice_fx/cough` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier/voice_fx/death` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier/voice_fx/downed` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier/voice_fx/fall` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier/voice_fx/hit` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier/voice_fx/melee` | Distance |
| `event:/infantry/enemy/walker/ww2_female_soldier01/voice_fx/bodyfall` | Distance |
| `event:/infantry/enemy/walker/ww2_female_soldier01/voice_fx/burning` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier01/voice_fx/cough` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier01/voice_fx/death` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier01/voice_fx/downed` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier01/voice_fx/fall` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier01/voice_fx/hit` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier01/voice_fx/melee` | Distance |
| `event:/infantry/enemy/walker/ww2_female_soldier02/voice_fx/bodyfall` | Distance |
| `event:/infantry/enemy/walker/ww2_female_soldier02/voice_fx/burning` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier02/voice_fx/cough` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier02/voice_fx/death` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier02/voice_fx/downed` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier02/voice_fx/fall` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier02/voice_fx/hit` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier02/voice_fx/melee` | Distance |
| `event:/infantry/enemy/walker/ww2_female_soldier03/voice_fx/bodyfall` | Distance |
| `event:/infantry/enemy/walker/ww2_female_soldier03/voice_fx/burning` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier03/voice_fx/cough` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier03/voice_fx/death` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier03/voice_fx/downed` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier03/voice_fx/fall` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier03/voice_fx/hit` |  |
| `event:/infantry/enemy/walker/ww2_female_soldier03/voice_fx/melee` | Distance |
| `event:/infantry/enemy/walker/ww2_jp_soldier/voice_fx/bodyfall` | Distance |
| `event:/infantry/enemy/walker/ww2_jp_soldier/voice_fx/burning` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier/voice_fx/cough` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier/voice_fx/death` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier/voice_fx/downed` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier/voice_fx/fall` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier/voice_fx/hit` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier/voice_fx/melee` | Distance |
| `event:/infantry/enemy/walker/ww2_jp_soldier01/voice_fx/bodyfall` | Distance |
| `event:/infantry/enemy/walker/ww2_jp_soldier01/voice_fx/burning` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier01/voice_fx/cough` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier01/voice_fx/death` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier01/voice_fx/downed` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier01/voice_fx/fall` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier01/voice_fx/hit` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier01/voice_fx/melee` | Distance |
| `event:/infantry/enemy/walker/ww2_jp_soldier02/voice_fx/bodyfall` | Distance |
| `event:/infantry/enemy/walker/ww2_jp_soldier02/voice_fx/burning` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier02/voice_fx/cough` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier02/voice_fx/death` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier02/voice_fx/downed` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier02/voice_fx/fall` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier02/voice_fx/hit` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier02/voice_fx/melee` | Distance |
| `event:/infantry/enemy/walker/ww2_jp_soldier03/voice_fx/bodyfall` | Distance |
| `event:/infantry/enemy/walker/ww2_jp_soldier03/voice_fx/burning` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier03/voice_fx/cough` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier03/voice_fx/death` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier03/voice_fx/downed` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier03/voice_fx/fall` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier03/voice_fx/hit` |  |
| `event:/infantry/enemy/walker/ww2_jp_soldier03/voice_fx/melee` | Distance |
| `event:/infantry/enemy/walker/ww2_soldier/voice_fx/bodyfall` | Distance |
| `event:/infantry/enemy/walker/ww2_soldier/voice_fx/burning` |  |
| `event:/infantry/enemy/walker/ww2_soldier/voice_fx/cough` |  |
| `event:/infantry/enemy/walker/ww2_soldier/voice_fx/death` |  |
| `event:/infantry/enemy/walker/ww2_soldier/voice_fx/downed` |  |
| `event:/infantry/enemy/walker/ww2_soldier/voice_fx/fall` |  |
| `event:/infantry/enemy/walker/ww2_soldier/voice_fx/hit` |  |
| `event:/infantry/enemy/walker/ww2_soldier/voice_fx/melee` | Distance |
| `event:/infantry/enemy/walker/ww2_soldier01/voice_fx/bodyfall` | Distance |
| `event:/infantry/enemy/walker/ww2_soldier01/voice_fx/burning` |  |
| `event:/infantry/enemy/walker/ww2_soldier01/voice_fx/cough` |  |
| `event:/infantry/enemy/walker/ww2_soldier01/voice_fx/death` |  |
| `event:/infantry/enemy/walker/ww2_soldier01/voice_fx/downed` |  |
| `event:/infantry/enemy/walker/ww2_soldier01/voice_fx/fall` |  |
| `event:/infantry/enemy/walker/ww2_soldier01/voice_fx/hit` |  |
| `event:/infantry/enemy/walker/ww2_soldier01/voice_fx/melee` | Distance |
| `event:/infantry/enemy/walker/ww2_soldier02/voice_fx/bodyfall` | Distance |
| `event:/infantry/enemy/walker/ww2_soldier02/voice_fx/burning` |  |
| `event:/infantry/enemy/walker/ww2_soldier02/voice_fx/cough` |  |
| `event:/infantry/enemy/walker/ww2_soldier02/voice_fx/death` |  |
| `event:/infantry/enemy/walker/ww2_soldier02/voice_fx/downed` |  |
| `event:/infantry/enemy/walker/ww2_soldier02/voice_fx/fall` |  |
| `event:/infantry/enemy/walker/ww2_soldier02/voice_fx/hit` |  |
| `event:/infantry/enemy/walker/ww2_soldier02/voice_fx/melee` | Distance |
| `event:/infantry/enemy/walker/ww2_soldier03/voice_fx/bodyfall` | Distance |
| `event:/infantry/enemy/walker/ww2_soldier03/voice_fx/burning` |  |
| `event:/infantry/enemy/walker/ww2_soldier03/voice_fx/cough` |  |
| `event:/infantry/enemy/walker/ww2_soldier03/voice_fx/death` |  |
| `event:/infantry/enemy/walker/ww2_soldier03/voice_fx/downed` |  |
| `event:/infantry/enemy/walker/ww2_soldier03/voice_fx/fall` |  |
| `event:/infantry/enemy/walker/ww2_soldier03/voice_fx/hit` |  |
| `event:/infantry/enemy/walker/ww2_soldier03/voice_fx/melee` | Distance |
| `event:/infantry/player/walker/mc_soldier/voice_fx/bleed_out` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/bodyfall` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/breath/aim_off` | noairtime |
| `event:/infantry/player/walker/mc_soldier/voice_fx/breath/aim_on` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/breath/in` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/breath/inhale` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/breath/out` | noairtime |
| `event:/infantry/player/walker/mc_soldier/voice_fx/breath/sprint` | on_step, stamina |
| `event:/infantry/player/walker/mc_soldier/voice_fx/breath/stamina_out` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/burning` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/contused` | intensity |
| `event:/infantry/player/walker/mc_soldier/voice_fx/cough` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/death` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/downed` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/drown` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/fall` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/hit` |  |
| `event:/infantry/player/walker/mc_soldier/voice_fx/melee` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/bodyfall` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/breath/aim_off` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/breath/aim_on` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/breath/in` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/breath/inhale` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/breath/out` | noairtime |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/breath/sprint` | stamina |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/breath/stamina_out` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/burning` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/contused` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/cough` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/death` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/downed` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/drown` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/fall` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/hit` |  |
| `event:/infantry/player/walker/ww2_female_soldier/voice_fx/melee` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/bodyfall` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/breath/aim_off` | noairtime |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/breath/aim_on` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/breath/in` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/breath/inhale` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/breath/out` | noairtime |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/breath/sprint` | stamina |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/breath/stamina_out` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/burning` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/contused` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/cough` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/death` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/downed` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/drown` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/fall` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/hit` |  |
| `event:/infantry/player/walker/ww2_jp_soldier/voice_fx/melee` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/bodyfall` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/breath/aim_off` | noairtime |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/breath/aim_on` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/breath/in` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/breath/inhale` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/breath/out` | noairtime |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/breath/sprint` | stamina |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/breath/stamina_out` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/burning` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/contused` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/cough` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/death` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/downed` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/drown` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/fall` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/hit` |  |
| `event:/infantry/player/walker/ww2_soldier/voice_fx/melee` |  |
| `event:/infantry/vo/enemy/mc/soldier01/en/enemy_warning_ahead` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier01/en/enemy_warning_behind` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier01/en/enemy_warning_left` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier01/en/enemy_warning_right` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier01/en/explosion_throw` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier01/en/friendly_fire` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier01/en/grenade_throw` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier01/en/help` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier01/en/molotov_throw` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier01/en/order_accept` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier01/en/qm_accept` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier01/en/qm_decline` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier01/en/qm_sorry` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier01/en/qm_thanks` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier01/en/qm_well_done` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier01/en/sniper_warning_ahead` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier01/en/sniper_warning_behind` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier01/en/sniper_warning_left` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier01/en/sniper_warning_right` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier01/en/squad_member_killed` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier01/ru/enemy_warning_ahead` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier01/ru/enemy_warning_behind` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier01/ru/enemy_warning_left` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier01/ru/enemy_warning_right` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier01/ru/explosion_throw` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier01/ru/friendly_fire` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier01/ru/grenade_throw` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier01/ru/help` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier01/ru/molotov_throw` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier01/ru/order_accept` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier01/ru/qm_accept` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier01/ru/qm_decline` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier01/ru/qm_sorry` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier01/ru/qm_thanks` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier01/ru/qm_well_done` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier01/ru/sniper_warning_ahead` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier01/ru/sniper_warning_behind` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier01/ru/sniper_warning_left` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier01/ru/sniper_warning_right` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier01/ru/squad_member_killed` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier02/en/enemy_warning_ahead` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier02/en/enemy_warning_behind` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier02/en/enemy_warning_left` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier02/en/enemy_warning_right` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier02/en/explosion_throw` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier02/en/friendly_fire` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier02/en/grenade_throw` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier02/en/help` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier02/en/molotov_throw` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier02/en/order_accept` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier02/en/qm_accept` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier02/en/qm_decline` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier02/en/qm_sorry` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier02/en/qm_thanks` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier02/en/qm_well_done` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier02/en/sniper_warning_ahead` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier02/en/sniper_warning_behind` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier02/en/sniper_warning_left` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier02/en/sniper_warning_right` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier02/en/squad_member_killed` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier02/ru/enemy_warning_ahead` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier02/ru/enemy_warning_behind` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier02/ru/enemy_warning_left` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier02/ru/enemy_warning_right` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier02/ru/explosion_throw` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier02/ru/friendly_fire` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier02/ru/grenade_throw` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier02/ru/help` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier02/ru/molotov_throw` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier02/ru/order_accept` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier02/ru/qm_accept` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier02/ru/qm_decline` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier02/ru/qm_sorry` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier02/ru/qm_thanks` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier02/ru/qm_well_done` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier02/ru/sniper_warning_ahead` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier02/ru/sniper_warning_behind` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier02/ru/sniper_warning_left` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier02/ru/sniper_warning_right` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier02/ru/squad_member_killed` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/en/enemy_warning_ahead` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier03/en/enemy_warning_behind` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/en/enemy_warning_left` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier03/en/enemy_warning_right` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier03/en/explosion_throw` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/en/friendly_fire` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/en/grenade_throw` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier03/en/help` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/en/molotov_throw` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/en/order_accept` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/en/qm_accept` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/en/qm_decline` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier03/en/qm_sorry` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/en/qm_thanks` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/en/qm_well_done` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier03/en/sniper_warning_ahead` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/en/sniper_warning_behind` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier03/en/sniper_warning_left` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/en/sniper_warning_right` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/en/squad_member_killed` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier03/ru/enemy_warning_ahead` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/ru/enemy_warning_behind` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/ru/enemy_warning_left` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/ru/enemy_warning_right` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier03/ru/explosion_throw` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/ru/friendly_fire` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier03/ru/grenade_throw` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/ru/help` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/ru/molotov_throw` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/ru/order_accept` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier03/ru/qm_accept` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/ru/qm_decline` | friendly, reverbIndoor, Distance, occlusion |
| `event:/infantry/vo/enemy/mc/soldier03/ru/qm_sorry` | Distance, occlusion, friendly, reverbIndoor |
| `event:/infantry/vo/enemy/mc/soldier03/ru/qm_thanks` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/ru/qm_well_done` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/ru/sniper_warning_ahead` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/ru/sniper_warning_behind` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/enemy/mc/soldier03/ru/sniper_warning_left` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/ru/sniper_warning_right` | occlusion, Distance, reverbIndoor, friendly |
| `event:/infantry/vo/enemy/mc/soldier03/ru/squad_member_killed` | reverbIndoor, friendly, occlusion, Distance |
| `event:/infantry/vo/player/mc/player/en/art_command` |  |
| `event:/infantry/vo/player/mc/player/en/art_shoot` |  |
| `event:/infantry/vo/player/mc/player/en/capturing_ally` |  |
| `event:/infantry/vo/player/mc/player/en/capturing_enemy` |  |
| `event:/infantry/vo/player/mc/player/en/concealed_fire_warning` |  |
| `event:/infantry/vo/player/mc/player/en/enemy_hit` |  |
| `event:/infantry/vo/player/mc/player/en/enemy_kill` |  |
| `event:/infantry/vo/player/mc/player/en/enemy_machinegun` |  |
| `event:/infantry/vo/player/mc/player/en/enemy_tank` |  |
| `event:/infantry/vo/player/mc/player/en/enemy_warning` |  |
| `event:/infantry/vo/player/mc/player/en/explosion_throw` |  |
| `event:/infantry/vo/player/mc/player/en/fire_warning` |  |
| `event:/infantry/vo/player/mc/player/en/flash_grenade_throw` |  |
| `event:/infantry/vo/player/mc/player/en/flash_grenade_warning` |  |
| `event:/infantry/vo/player/mc/player/en/grenade_throw` |  |
| `event:/infantry/vo/player/mc/player/en/grenade_warning` |  |
| `event:/infantry/vo/player/mc/player/en/help` |  |
| `event:/infantry/vo/player/mc/player/en/hit` |  |
| `event:/infantry/vo/player/mc/player/en/hooray` |  |
| `event:/infantry/vo/player/mc/player/en/kill_grenade` |  |
| `event:/infantry/vo/player/mc/player/en/last_shot` |  |
| `event:/infantry/vo/player/mc/player/en/left_alone` |  |
| `event:/infantry/vo/player/mc/player/en/low_ammo` |  |
| `event:/infantry/vo/player/mc/player/en/molotov_throw` |  |
| `event:/infantry/vo/player/mc/player/en/point_captured` |  |
| `event:/infantry/vo/player/mc/player/en/qm_accept` |  |
| `event:/infantry/vo/player/mc/player/en/qm_cover_me` |  |
| `event:/infantry/vo/player/mc/player/en/qm_decline` |  |
| `event:/infantry/vo/player/mc/player/en/qm_sorry` |  |
| `event:/infantry/vo/player/mc/player/en/qm_thanks` |  |
| `event:/infantry/vo/player/mc/player/en/qm_well_done` |  |
| `event:/infantry/vo/player/mc/player/en/reloading` |  |
| `event:/infantry/vo/player/mc/player/en/smoke_grenade_throw` |  |
| `event:/infantry/vo/player/mc/player/en/smoke_grenade_warning` |  |
| `event:/infantry/vo/player/mc/player/en/sniper_warning` |  |
| `event:/infantry/vo/player/mc/player/en/tank_crew_player_tank_hit` |  |
| `event:/infantry/vo/player/mc/player/ru/art_command` |  |
| `event:/infantry/vo/player/mc/player/ru/art_shoot` |  |
| `event:/infantry/vo/player/mc/player/ru/capturing_ally` |  |
| `event:/infantry/vo/player/mc/player/ru/capturing_enemy` |  |
| `event:/infantry/vo/player/mc/player/ru/concealed_fire_warning` |  |
| `event:/infantry/vo/player/mc/player/ru/enemy_hit` |  |
| `event:/infantry/vo/player/mc/player/ru/enemy_kill` |  |
| `event:/infantry/vo/player/mc/player/ru/enemy_machinegun` |  |
| `event:/infantry/vo/player/mc/player/ru/enemy_tank` |  |
| `event:/infantry/vo/player/mc/player/ru/enemy_warning` |  |
| `event:/infantry/vo/player/mc/player/ru/explosion_throw` |  |
| `event:/infantry/vo/player/mc/player/ru/fire_warning` |  |
| `event:/infantry/vo/player/mc/player/ru/flash_grenade_throw` |  |
| `event:/infantry/vo/player/mc/player/ru/flash_grenade_warning` |  |
| `event:/infantry/vo/player/mc/player/ru/grenade_throw` |  |
| `event:/infantry/vo/player/mc/player/ru/grenade_warning` |  |
| `event:/infantry/vo/player/mc/player/ru/help` |  |
| `event:/infantry/vo/player/mc/player/ru/hit` |  |
| `event:/infantry/vo/player/mc/player/ru/hooray` |  |
| `event:/infantry/vo/player/mc/player/ru/kill_grenade` |  |
| `event:/infantry/vo/player/mc/player/ru/last_shot` |  |
| `event:/infantry/vo/player/mc/player/ru/left_alone` |  |
| `event:/infantry/vo/player/mc/player/ru/low_ammo` |  |
| `event:/infantry/vo/player/mc/player/ru/molotov_throw` |  |
| `event:/infantry/vo/player/mc/player/ru/point_captured` |  |
| `event:/infantry/vo/player/mc/player/ru/qm_accept` |  |
| `event:/infantry/vo/player/mc/player/ru/qm_cover_me` |  |
| `event:/infantry/vo/player/mc/player/ru/qm_decline` |  |
| `event:/infantry/vo/player/mc/player/ru/qm_sorry` |  |
| `event:/infantry/vo/player/mc/player/ru/qm_thanks` |  |
| `event:/infantry/vo/player/mc/player/ru/qm_well_done` |  |
| `event:/infantry/vo/player/mc/player/ru/reloading` |  |
| `event:/infantry/vo/player/mc/player/ru/smoke_grenade_throw` |  |
| `event:/infantry/vo/player/mc/player/ru/smoke_grenade_warning` |  |
| `event:/infantry/vo/player/mc/player/ru/sniper_warning` |  |
| `event:/infantry/vo/player/mc/player/ru/tank_crew_player_tank_hit` |  |
| `event:/infantry/vo/sfx/mc/radio_button_ally` |  |
| `event:/infantry/vo/sfx/mc/radio_button_player` |  |
| `event:/infantry/vo/sfx/mc/radio_heli_engine` |  |
| `event:/infantry/vo/sfx/mc/radio_tank_engine` |  |

## infantry_voices_narrator

15 events (15 named), 0 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/infantry/vo/narrator/leave_area_warn` |  |
| `event:/infantry/vo/narrator/mission_start_add` |  |
| `event:/infantry/vo/narrator/pilot_capture_gm_ally` |  |
| `event:/infantry/vo/narrator/pilot_capture_gm_enemy` |  |
| `event:/infantry/vo/narrator/pilot_mission_complete` |  |
| `event:/infantry/vo/narrator/pilot_mission_fail` |  |
| `event:/infantry/vo/narrator/pilot_tickets_lead_continue_ally` |  |
| `event:/infantry/vo/narrator/pilot_tickets_lead_continue_enemy` |  |
| `event:/infantry/vo/narrator/pilot_tickets_lead_start_ally` |  |
| `event:/infantry/vo/narrator/pilot_tickets_lead_start_enemy` |  |
| `event:/infantry/vo/narrator/pilot_tickets_lead_zone_ally` |  |
| `event:/infantry/vo/narrator/pilot_tickets_lead_zone_enemy` |  |
| `event:/infantry/vo/narrator/point_capturing_ally` |  |
| `event:/infantry/vo/narrator/point_capturing_enemy` |  |
| `event:/infantry/vo/narrator/point_capturing_player` |  |

## infantry_weapon

297 events (279 named), 5517 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun1_shot` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun2_shot` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun3_shot` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun4_shot` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun5_shot` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun6_shot` |  |
| `event:/infantry/enemy/weapon/_common/shot_antivehicle_far` |  |
| `event:/infantry/enemy/weapon/_common/shot_antivehicle_javelin_far` |  |
| `event:/infantry/enemy/weapon/_common/shot_loop_fast_far` |  |
| `event:/infantry/enemy/weapon/_common/shot_loop_gatling_far` | Distance |
| `event:/infantry/enemy/weapon/_common/shot_loop_low_far` |  |
| `event:/infantry/enemy/weapon/_common/shot_loop_mid_far` |  |
| `event:/infantry/enemy/weapon/_common/shot_mgun_far` |  |
| `event:/infantry/enemy/weapon/_common/shot_pistol_far` |  |
| `event:/infantry/enemy/weapon/_common/shot_rifle_far` |  |
| `event:/infantry/enemy/weapon/_common/shot_sniper_rifle_far` | Distance, Event Cone Angle |
| `event:/infantry/enemy/weapon/_common/tail_pistol` |  |
| `event:/infantry/enemy/weapon/_common/tail_pistol_far` |  |
| `event:/infantry/enemy/weapon/_common/tail_rifle` |  |
| `event:/infantry/enemy/weapon/_common/tail_rifle_add` |  |
| `event:/infantry/enemy/weapon/_common/tail_rifle_far` |  |
| `event:/infantry/enemy/weapon/antivehicle/fim_92a_stinger/shot_grains` | Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction, occlusion, Event Cone Angle, on_shot, headphones |
| `event:/infantry/enemy/weapon/antivehicle/gp_34/shot_grains` | isPlayerIndoor, Distance, Direction, Elevation, reverbIndoor, on_shot, headphones, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/antivehicle/gp_34/shot_single` | Event Cone Angle, occlusion, on_shot, headphones, reverbIndoor, Elevation, Distance, Direction, isPlayerIndoor |
| `event:/infantry/enemy/weapon/antivehicle/m136_at4/shot_grains` | isPlayerIndoor, Direction, Distance, Elevation, reverbIndoor, headphones, on_shot, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/antivehicle/m203/shot_grains` | isPlayerIndoor, Direction, Distance, Elevation, reverbIndoor, headphones, on_shot, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/antivehicle/m203/shot_single` | occlusion, Event Cone Angle, on_shot, headphones, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction |
| `event:/infantry/enemy/weapon/antivehicle/mpads_verba/shot_grains` | isPlayerIndoor, Distance, Direction, Elevation, reverbIndoor, on_shot, headphones, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/antivehicle/rpg_7/shot_grains` | reverbIndoor, Elevation, Direction, Distance, isPlayerIndoor, Event Cone Angle, occlusion, headphones, on_shot |
| `event:/infantry/enemy/weapon/mgun/ab_46/shot_grains` | headphones, Event Cone Angle, occlusion, Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot |
| `event:/infantry/enemy/weapon/mgun/ab_46/suppressed/shot_grains` | headphones, Event Cone Angle, occlusion, Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot |
| `event:/infantry/enemy/weapon/mgun/ak_12/shot_grains` | isPlayerIndoor, Distance, Direction, on_shot, Elevation, reverbIndoor, headphones, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/mgun/ak_12/suppressed/shot_grains` | Event Cone Angle, occlusion, headphones, reverbIndoor, Elevation, on_shot, Direction, Distance, isPlayerIndoor |
| `event:/infantry/enemy/weapon/mgun/ak_15/shot_grains` | headphones, Event Cone Angle, occlusion, Distance, Direction, isPlayerIndoor, reverbIndoor, on_shot, Elevation |
| `event:/infantry/enemy/weapon/mgun/ak_15/suppressed/shot_grains` | reverbIndoor, on_shot, Elevation, Distance, Direction, isPlayerIndoor, Event Cone Angle, occlusion, headphones |
| `event:/infantry/enemy/weapon/mgun/ak_47/shot_grains` | headphones, Event Cone Angle, occlusion, Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot |
| `event:/infantry/enemy/weapon/mgun/ak_47/suppressed/shot_grains` | isPlayerIndoor, Distance, Direction, on_shot, Elevation, reverbIndoor, headphones, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/mgun/ak_74/shot_grains` | on_shot, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction, occlusion, Event Cone Angle, headphones |
| `event:/infantry/enemy/weapon/mgun/ak_74/suppressed/shot_grains` | reverbIndoor, on_shot, Elevation, Distance, Direction, isPlayerIndoor, Event Cone Angle, occlusion, headphones |
| `event:/infantry/enemy/weapon/mgun/akm/shot_grains` | isPlayerIndoor, Direction, Distance, Elevation, on_shot, reverbIndoor, headphones, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/mgun/akm/suppressed/shot_grains` | headphones, Event Cone Angle, occlusion, Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot |
| `event:/infantry/enemy/weapon/mgun/aks_74u/shot_grains` | Event Cone Angle, occlusion, headphones, reverbIndoor, Elevation, on_shot, Direction, Distance, isPlayerIndoor |
| `event:/infantry/enemy/weapon/mgun/aks_74u/suppressed/shot_grains` | Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/an_94/shot_grains` | Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/an_94/suppressed/shot_grains` | reverbIndoor, Elevation, on_shot, Direction, Distance, isPlayerIndoor, Event Cone Angle, occlusion, headphones |
| `event:/infantry/enemy/weapon/mgun/as_44/shot_grains` | headphones, Event Cone Angle, occlusion, Distance, Direction, isPlayerIndoor, reverbIndoor, on_shot, Elevation |
| `event:/infantry/enemy/weapon/mgun/as_val/shot_grains` | occlusion, Event Cone Angle, headphones, Elevation, on_shot, reverbIndoor, isPlayerIndoor, Direction, Distance |
| `event:/infantry/enemy/weapon/mgun/avs36/shot_grains` | isPlayerIndoor, Direction, Distance, Elevation, on_shot, reverbIndoor, headphones, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/mgun/colt_9_mm_smg/shot_grains` | on_shot, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction, occlusion, Event Cone Angle, headphones |
| `event:/infantry/enemy/weapon/mgun/colt_9_mm_smg/suppressed/shot_grains` | on_shot, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction, occlusion, Event Cone Angle, headphones |
| `event:/infantry/enemy/weapon/mgun/dpm/shot_grains` | headphones, Event Cone Angle, occlusion, Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot |
| `event:/infantry/enemy/weapon/mgun/fn_scar_h/shot_grains` | isPlayerIndoor, Distance, Direction, on_shot, Elevation, reverbIndoor, headphones, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/mgun/fn_scar_h/suppressed/shot_grains` | Elevation, on_shot, reverbIndoor, isPlayerIndoor, Direction, Distance, occlusion, Event Cone Angle, headphones |
| `event:/infantry/enemy/weapon/mgun/fn_scar_l/shot_grains` | headphones, Event Cone Angle, occlusion, Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot |
| `event:/infantry/enemy/weapon/mgun/fn_scar_l/suppressed/shot_grains` | reverbIndoor, on_shot, Elevation, Distance, Direction, isPlayerIndoor, Event Cone Angle, occlusion, headphones |
| `event:/infantry/enemy/weapon/mgun/hk_mp5/shot_grains` | Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/hk_mp5/suppressed/shot_grains` | occlusion, Event Cone Angle, headphones, on_shot, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction |
| `event:/infantry/enemy/weapon/mgun/kord_6p68/shot_grains` | headphones, occlusion, Event Cone Angle, isPlayerIndoor, Direction, Distance, Elevation, on_shot, reverbIndoor |
| `event:/infantry/enemy/weapon/mgun/kord_6p68/suppressed/shot_grains` | Elevation, on_shot, reverbIndoor, isPlayerIndoor, Direction, Distance, occlusion, Event Cone Angle, headphones |
| `event:/infantry/enemy/weapon/mgun/m14/shot_grains` | Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/m14/suppressed/shot_grains` | headphones, Event Cone Angle, occlusion, Distance, Direction, isPlayerIndoor, reverbIndoor, on_shot, Elevation |
| `event:/infantry/enemy/weapon/mgun/m16a4/shot_grains` | headphones, Event Cone Angle, occlusion, Distance, Direction, isPlayerIndoor, reverbIndoor, on_shot, Elevation |
| `event:/infantry/enemy/weapon/mgun/m16a4/suppressed/shot_grains` | Elevation, on_shot, reverbIndoor, isPlayerIndoor, Direction, Distance, occlusion, Event Cone Angle, headphones |
| `event:/infantry/enemy/weapon/mgun/m1918/shot_grains` | isPlayerIndoor, Direction, Distance, Elevation, on_shot, reverbIndoor, headphones, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/mgun/m1918/suppressed/shot_grains` | occlusion, Event Cone Angle, headphones, on_shot, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction |
| `event:/infantry/enemy/weapon/mgun/m1919a6/shot_grains` | occlusion, Event Cone Angle, headphones, on_shot, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction |
| `event:/infantry/enemy/weapon/mgun/m1919a6/suppressed/shot_grains` | Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/m240/shot_grains` | reverbIndoor, on_shot, Elevation, Distance, Direction, isPlayerIndoor, Event Cone Angle, occlusion, headphones |
| `event:/infantry/enemy/weapon/mgun/m240/suppressed/shot_grains` | on_shot, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction, occlusion, Event Cone Angle, headphones |
| `event:/infantry/enemy/weapon/mgun/m249/shot_grains` | headphones, Event Cone Angle, occlusion, Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot |
| `event:/infantry/enemy/weapon/mgun/m27_iar/shot_grains` | reverbIndoor, Elevation, on_shot, Direction, Distance, isPlayerIndoor, Event Cone Angle, occlusion, headphones |
| `event:/infantry/enemy/weapon/mgun/m27_iar/suppressed/shot_grains` | Elevation, on_shot, reverbIndoor, isPlayerIndoor, Direction, Distance, occlusion, Event Cone Angle, headphones |
| `event:/infantry/enemy/weapon/mgun/m3/shot_grains` | Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/m3/suppressed/shot_grains` | Event Cone Angle, occlusion, headphones, reverbIndoor, Elevation, on_shot, Direction, Distance, isPlayerIndoor |
| `event:/infantry/enemy/weapon/mgun/m4a1/shot_grains` | occlusion, Event Cone Angle, headphones, Elevation, on_shot, reverbIndoor, isPlayerIndoor, Direction, Distance |
| `event:/infantry/enemy/weapon/mgun/m4a1/suppressed/shot_grains` | headphones, Event Cone Angle, occlusion, Distance, Direction, isPlayerIndoor, reverbIndoor, on_shot, Elevation |
| `event:/infantry/enemy/weapon/mgun/mac_11/shot_grains` | on_shot, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction, occlusion, Event Cone Angle, headphones |
| `event:/infantry/enemy/weapon/mgun/mac_11/suppressed/shot_grains` | isPlayerIndoor, Distance, Direction, on_shot, Elevation, reverbIndoor, headphones, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/mgun/mk_48/shot_grains` | reverbIndoor, on_shot, Elevation, Distance, Direction, isPlayerIndoor, Event Cone Angle, occlusion, headphones |
| `event:/infantry/enemy/weapon/mgun/mk_48/suppressed/shot_grains` | reverbIndoor, on_shot, Elevation, Distance, Direction, isPlayerIndoor, Event Cone Angle, occlusion, headphones |
| `event:/infantry/enemy/weapon/mgun/pkp_pecheneg/shot_grains` | headphones, Event Cone Angle, occlusion, Distance, Direction, isPlayerIndoor, reverbIndoor, on_shot, Elevation |
| `event:/infantry/enemy/weapon/mgun/pkp_pecheneg/suppressed/shot_grains` | Elevation, on_shot, reverbIndoor, isPlayerIndoor, Direction, Distance, occlusion, Event Cone Angle, headphones |
| `event:/infantry/enemy/weapon/mgun/pp_19_vityaz/shot_grains` | headphones, Event Cone Angle, occlusion, Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot |
| `event:/infantry/enemy/weapon/mgun/pp_19_vityaz/suppressed/shot_grains` | Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_2000/shot_grains` | reverbIndoor, on_shot, Elevation, Distance, Direction, isPlayerIndoor, Event Cone Angle, occlusion, headphones |
| `event:/infantry/enemy/weapon/mgun/pp_2000/suppressed/shot_grains` | headphones, Event Cone Angle, occlusion, Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot |
| `event:/infantry/enemy/weapon/mgun/pp_71/shot_grains` | Event Cone Angle, occlusion, headphones, reverbIndoor, on_shot, Elevation, Distance, Direction, isPlayerIndoor |
| `event:/infantry/enemy/weapon/mgun/pp_71/suppressed/shot_grains` | reverbIndoor, Elevation, on_shot, Direction, Distance, isPlayerIndoor, Event Cone Angle, occlusion, headphones |
| `event:/infantry/enemy/weapon/mgun/pps_42/shot_grains` | on_shot, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction, occlusion, Event Cone Angle, headphones |
| `event:/infantry/enemy/weapon/mgun/pps_42/suppressed/shot_grains` | Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/ppsh/shot_grains` | occlusion, Event Cone Angle, headphones, on_shot, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction |
| `event:/infantry/enemy/weapon/mgun/ppsh/suppressed/shot_grains` | Distance, Direction, isPlayerIndoor, reverbIndoor, on_shot, Elevation, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/rd_44/shot_grains` | occlusion, Event Cone Angle, headphones, Elevation, on_shot, reverbIndoor, isPlayerIndoor, Direction, Distance |
| `event:/infantry/enemy/weapon/mgun/rp_46/shot_grains` | headphones, Event Cone Angle, occlusion, Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot |
| `event:/infantry/enemy/weapon/mgun/rpk_16/shot_grains` | on_shot, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction, occlusion, Event Cone Angle, headphones |
| `event:/infantry/enemy/weapon/mgun/rpk_16/suppressed/shot_grains` | Event Cone Angle, occlusion, headphones, reverbIndoor, Elevation, on_shot, Direction, Distance, isPlayerIndoor |
| `event:/infantry/enemy/weapon/mgun/rpk_74m/shot_grains` | headphones, Event Cone Angle, occlusion, Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot |
| `event:/infantry/enemy/weapon/mgun/rpk_74m/suppressed/shot_grains` | Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/shot_grains` | Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/suppressed/shot_grains` | headphones, occlusion, Event Cone Angle, isPlayerIndoor, Distance, Direction, on_shot, Elevation, reverbIndoor |
| `event:/infantry/enemy/weapon/mgun/sig_xm5/shot_grains` | occlusion, Event Cone Angle, headphones, on_shot, Elevation, reverbIndoor, isPlayerIndoor, Distance, Direction |
| `event:/infantry/enemy/weapon/mgun/sig_xm5/suppressed/shot_grains` | Distance, Direction, isPlayerIndoor, reverbIndoor, on_shot, Elevation, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson/shot_grains` | reverbIndoor, on_shot, Elevation, Distance, Direction, isPlayerIndoor, Event Cone Angle, occlusion, headphones |
| `event:/infantry/enemy/weapon/mgun/thompson/suppressed/shot_grains` | headphones, occlusion, Event Cone Angle, isPlayerIndoor, Direction, Distance, Elevation, on_shot, reverbIndoor |
| `event:/infantry/enemy/weapon/mgun/thompson_m1921ac/shot_grains` | Distance, Direction, isPlayerIndoor, reverbIndoor, on_shot, Elevation, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_m1921ac/suppressed/shot_grains` | headphones, occlusion, Event Cone Angle, isPlayerIndoor, Distance, Direction, on_shot, Elevation, reverbIndoor |
| `event:/infantry/enemy/weapon/mgun/xm177e1/shot_grains` | Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation, on_shot, headphones, Event Cone Angle, occlusion |
| `event:/infantry/enemy/weapon/mgun/xm177e1/suppressed/shot_grains` | headphones, occlusion, Event Cone Angle, isPlayerIndoor, Distance, Direction, on_shot, Elevation, reverbIndoor |
| `event:/infantry/enemy/weapon/pistol/beretta_m9/shot_grains` | Event Cone Angle, occlusion, on_shot, headphones, reverbIndoor, Elevation, Distance, Direction, isPlayerIndoor |
| `event:/infantry/enemy/weapon/pistol/tt/shot_grains` | isPlayerIndoor, Distance, Direction, Elevation, reverbIndoor, on_shot, headphones, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/rifle/barrett_m82a1/shot_grains` | occlusion, Event Cone Angle, headphones, on_shot, Elevation, reverbIndoor, isPlayerIndoor, Direction, Distance |
| `event:/infantry/enemy/weapon/rifle/ks_p_18_5/shot_grains` | on_shot, headphones, Event Cone Angle, occlusion, Distance, Direction, isPlayerIndoor, reverbIndoor, Elevation |
| `event:/infantry/enemy/weapon/rifle/ksvk_12_7/shot_grains` | Event Cone Angle, occlusion, headphones, on_shot, reverbIndoor, Elevation, Direction, Distance, isPlayerIndoor |
| `event:/infantry/enemy/weapon/rifle/m110a1_sdmr/shot_grains` | reverbIndoor, Elevation, Direction, Distance, isPlayerIndoor, Event Cone Angle, occlusion, headphones, on_shot |
| `event:/infantry/enemy/weapon/rifle/m110a1_sdmr/suppressed/shot_grains` | isPlayerIndoor, Direction, Distance, Elevation, reverbIndoor, headphones, on_shot, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/rifle/m1903_springfield/shot_grains` | Event Cone Angle, occlusion, headphones, on_shot, reverbIndoor, Elevation, Direction, Distance, isPlayerIndoor |
| `event:/infantry/enemy/weapon/rifle/m1a1_carbine/shot_grains` | Event Cone Angle, occlusion, on_shot, headphones, reverbIndoor, Elevation, Distance, Direction, isPlayerIndoor |
| `event:/infantry/enemy/weapon/rifle/m24/shot_grains` | reverbIndoor, Elevation, Direction, Distance, isPlayerIndoor, Event Cone Angle, occlusion, headphones, on_shot |
| `event:/infantry/enemy/weapon/rifle/m24/suppressed/shot_grains` | reverbIndoor, Elevation, Direction, Distance, isPlayerIndoor, Event Cone Angle, occlusion, headphones, on_shot |
| `event:/infantry/enemy/weapon/rifle/mk_14_ebr/shot_grains` | isPlayerIndoor, Direction, Distance, Elevation, reverbIndoor, headphones, on_shot, occlusion, Event Cone Angle |
| `event:/infantry/enemy/weapon/rifle/mk_14_ebr/suppressed/shot_grains` | Elevation, reverbIndoor, isPlayerIndoor, Direction, Distance, occlusion, Event Cone Angle, headphones, on_shot |
| `event:/infantry/enemy/weapon/rifle/mosin_m44/shot_grains` | occlusion, Event Cone Angle, headphones, on_shot, Elevation, reverbIndoor, isPlayerIndoor, Direction, Distance |
| `event:/infantry/enemy/weapon/rifle/mossberg_590/shot_grains` | Event Cone Angle, occlusion, headphones, on_shot, reverbIndoor, Elevation, Direction, Distance, isPlayerIndoor |
| `event:/infantry/enemy/weapon/rifle/sks_44/shot_grains` | reverbIndoor, Elevation, Distance, Direction, isPlayerIndoor, Event Cone Angle, occlusion, on_shot, headphones |
| `event:/infantry/enemy/weapon/rifle/sv_98/shot_grains` | occlusion, Event Cone Angle, headphones, on_shot, Elevation, reverbIndoor, isPlayerIndoor, Direction, Distance |
| `event:/infantry/enemy/weapon/rifle/sv_98/suppressed/shot_grains` | Event Cone Angle, occlusion, on_shot, headphones, reverbIndoor, Elevation, Distance, Direction, isPlayerIndoor |
| `event:/infantry/enemy/weapon/rifle/svch/shot_grains` | on_shot, headphones, Event Cone Angle, occlusion, Distance, Direction, isPlayerIndoor, reverbIndoor, Elevation |
| `event:/infantry/enemy/weapon/rifle/svch/suppressed/shot_grains` | reverbIndoor, Elevation, Distance, Direction, isPlayerIndoor, Event Cone Angle, occlusion, on_shot, headphones |
| `event:/infantry/enemy/weapon/rifle/svd_m/shot_grains` | reverbIndoor, Elevation, Direction, Distance, isPlayerIndoor, Event Cone Angle, occlusion, headphones, on_shot |
| `event:/infantry/enemy/weapon/rifle/svd_m/suppressed/shot_grains` | on_shot, headphones, Event Cone Angle, occlusion, Distance, Direction, isPlayerIndoor, reverbIndoor, Elevation |
| `event:/infantry/enemy/weapon/rifle/svt40/shot_grains` | headphones, on_shot, Event Cone Angle, occlusion, Direction, Distance, isPlayerIndoor, reverbIndoor, Elevation |
| `event:/infantry/player/weapon/_common/shell_out` | mat |
| `event:/infantry/player/weapon/_common/shot_dry` |  |
| `event:/infantry/player/weapon/_common/shot_dry_flamethrower` |  |
| `event:/infantry/player/weapon/_common/shot_dry_pistol` |  |
| `event:/infantry/player/weapon/_common/shot_dry_rifle` |  |
| `event:/infantry/player/weapon/_common/shot_dry_small_cannon` |  |
| `event:/infantry/player/weapon/_common/tail_mgun` |  |
| `event:/infantry/player/weapon/antivehicle/fim_92a_stinger/shot_grains` | on_shot, reverbIndoor, mat |
| `event:/infantry/player/weapon/antivehicle/gp_34/shot_grains` | on_shot, reverbIndoor, mat, aiming |
| `event:/infantry/player/weapon/antivehicle/gp_34/shot_single` | reverbIndoor, mat, aiming |
| `event:/infantry/player/weapon/antivehicle/m136_at4/shot_grains` | reverbIndoor, mat, on_shot |
| `event:/infantry/player/weapon/antivehicle/m203/shot_grains` | mat, aiming, reverbIndoor, on_shot |
| `event:/infantry/player/weapon/antivehicle/m203/shot_single` | aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/antivehicle/mpads_verba/shot_grains` | on_shot, mat, reverbIndoor |
| `event:/infantry/player/weapon/antivehicle/rpg_7/shot_grains` | mat, reverbIndoor, on_shot |
| `event:/infantry/player/weapon/mgun/ab_46/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/mgun/ab_46/suppressed/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/mgun/ak_12/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/mgun/ak_12/suppressed/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/ak_15/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/mgun/ak_15/suppressed/shot_grains` | aiming, mat, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/ak_47/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/mgun/ak_47/suppressed/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/ak_74/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/mgun/ak_74/suppressed/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/akm/shot_grains` | reverbIndoor, on_shot, mat, aiming |
| `event:/infantry/player/weapon/mgun/akm/suppressed/shot_grains` | mat, aiming, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/aks_74u/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/mgun/aks_74u/suppressed/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/mgun/an_94/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/an_94/suppressed/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/as_44/shot_grains` | aiming, mat, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/as_val/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/mgun/avs36/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/mgun/colt_9_mm_smg/shot_grains` | reverbIndoor, mat, aiming, on_shot |
| `event:/infantry/player/weapon/mgun/colt_9_mm_smg/suppressed/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/mgun/dpm/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/mgun/fn_scar_h/shot_grains` | aiming, mat, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/fn_scar_h/suppressed/shot_grains` | reverbIndoor, on_shot, mat, aiming |
| `event:/infantry/player/weapon/mgun/fn_scar_l/shot_grains` | reverbIndoor, mat, aiming, on_shot |
| `event:/infantry/player/weapon/mgun/fn_scar_l/suppressed/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/mgun/hk_mp5/shot_grains` | mat, aiming, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/hk_mp5/suppressed/shot_grains` | reverbIndoor, mat, aiming, on_shot |
| `event:/infantry/player/weapon/mgun/kord_6p68/shot_grains` | mat, aiming, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/kord_6p68/suppressed/shot_grains` | reverbIndoor, on_shot, mat, aiming |
| `event:/infantry/player/weapon/mgun/m14/shot_grains` | aiming, mat, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/m14/suppressed/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/m16a4/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/m16a4/suppressed/shot_grains` | reverbIndoor, mat, aiming, on_shot |
| `event:/infantry/player/weapon/mgun/m1918/shot_grains` | reverbIndoor, on_shot, mat, aiming |
| `event:/infantry/player/weapon/mgun/m1918/suppressed/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/mgun/m1919a6/shot_grains` | mat, aiming, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/m1919a6/suppressed/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/mgun/m240/shot_grains` | aiming, mat, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/m249/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/mgun/m27_iar/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/m27_iar/suppressed/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/m3/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/mgun/m3/suppressed/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/mgun/m4a1/shot_grains` | reverbIndoor, mat, aiming, on_shot |
| `event:/infantry/player/weapon/mgun/m4a1/suppressed/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/mgun/mac_11/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/mgun/mac_11/suppressed/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/mgun/mk_48/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/mgun/pkp_pecheneg/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/mgun/pkp_pecheneg/suppressed/shot_grains` | reverbIndoor, on_shot, mat, aiming |
| `event:/infantry/player/weapon/mgun/pp_19_vityaz/shot_grains` | reverbIndoor, on_shot, mat, aiming |
| `event:/infantry/player/weapon/mgun/pp_19_vityaz/suppressed/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/mgun/pp_2000/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/pp_2000/suppressed/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/mgun/pp_71/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/pp_71/suppressed/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/pps_42/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/mgun/pps_42/suppressed/shot_grains` | mat, aiming, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/ppsh/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/ppsh/suppressed/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/mgun/rd_44/shot_grains` | reverbIndoor, on_shot, mat, aiming |
| `event:/infantry/player/weapon/mgun/rp_46/shot_grains` | mat, aiming, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/rpk_16/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/mgun/rpk_16/suppressed/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/mgun/rpk_74m/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/mgun/rpk_74m/suppressed/shot_grains` | mat, aiming, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/sig_xm250/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/sig_xm250/suppressed/shot_grains` | reverbIndoor, on_shot, aiming, mat |
| `event:/infantry/player/weapon/mgun/sig_xm5/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/mgun/sig_xm5/suppressed/shot_grains` | reverbIndoor, on_shot, mat, aiming |
| `event:/infantry/player/weapon/mgun/thompson/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/mgun/thompson/suppressed/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/mgun/thompson_m1921ac/shot_grains` | aiming, mat, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/thompson_m1921ac/suppressed/shot_grains` | reverbIndoor, mat, aiming, on_shot |
| `event:/infantry/player/weapon/mgun/xm177e1/shot_grains` | aiming, mat, on_shot, reverbIndoor |
| `event:/infantry/player/weapon/mgun/xm177e1/suppressed/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/pistol/beretta_m9/shot_grains` | reverbIndoor, mat, aiming, on_shot |
| `event:/infantry/player/weapon/pistol/tt/shot_grains` | reverbIndoor, mat, aiming, on_shot |
| `event:/infantry/player/weapon/rifle/barrett_m82a1/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/rifle/ks_p_18_5/shot_grains` | aiming, mat, reverbIndoor, on_shot |
| `event:/infantry/player/weapon/rifle/ksvk_12_7/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/rifle/m110a1_sdmr/shot_grains` | mat, aiming, reverbIndoor, on_shot |
| `event:/infantry/player/weapon/rifle/m110a1_sdmr/suppressed/shot_grains` | on_shot, reverbIndoor, mat, aiming |
| `event:/infantry/player/weapon/rifle/m1903_springfield/shot_grains` | mat, aiming, reverbIndoor, on_shot |
| `event:/infantry/player/weapon/rifle/m1a1_carbine/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/rifle/m24/shot_grains` | reverbIndoor, mat, aiming, on_shot |
| `event:/infantry/player/weapon/rifle/m24/suppressed/shot_grains` | mat, aiming, reverbIndoor, on_shot |
| `event:/infantry/player/weapon/rifle/mk_14_ebr/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/rifle/mk_14_ebr/suppressed/shot_grains` | on_shot, reverbIndoor, aiming, mat |
| `event:/infantry/player/weapon/rifle/mosin_m44/shot_grains` | reverbIndoor, aiming, mat, on_shot |
| `event:/infantry/player/weapon/rifle/mossberg_590/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/player/weapon/rifle/sks_44/shot_grains` | on_shot, reverbIndoor, mat, aiming |
| `event:/infantry/player/weapon/rifle/sv_98/shot_grains` | mat, aiming, reverbIndoor, on_shot |
| `event:/infantry/player/weapon/rifle/sv_98/suppressed/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/rifle/svch/shot_grains` | aiming, mat, reverbIndoor, on_shot |
| `event:/infantry/player/weapon/rifle/svch/suppressed/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/rifle/svd_m/shot_grains` | on_shot, aiming, mat, reverbIndoor |
| `event:/infantry/player/weapon/rifle/svd_m/suppressed/shot_grains` | on_shot, reverbIndoor, aiming, mat |
| `event:/infantry/player/weapon/rifle/svt40/shot_grains` | on_shot, mat, aiming, reverbIndoor |
| `event:/infantry/weapon/atgm/roland/atgm_LPC` | Distance, building_density, on_shot, Event Cone Angle |
| `event:/infantry/weapon/atgm/roland/atgm_LPC_ai` | headphones, building_density, Direction, on_shot, Distance |
| `event:/infantry/weapon/atgm/roland/atgm_LPC_interior` | on_shot, Distance |
| `event:/infantry/weapon/cannons/120mm_Rh120` | Event Cone Angle, on_shot, multiply_weapon, Distance, building_density |
| `event:/infantry/weapon/cannons/120mm_Rh120_ai` | isPlayerIndoor, Distance, on_shot, building_density, Direction, headphones, Event Cone Angle |
| `event:/infantry/weapon/cannons/120mm_Rh120_interior` | Distance, on_shot |
| `event:/infantry/weapon/cannons/125mm_2a46_t72` | Event Cone Angle, on_shot, multiply_weapon, building_density, Distance |
| `event:/infantry/weapon/cannons/125mm_2a46_t72_ai` | headphones, Event Cone Angle, on_shot, Distance, isPlayerIndoor, Direction, building_density |
| `event:/infantry/weapon/cannons/125mm_2a46_t72_interior` | Distance, on_shot |
| `event:/infantry/weapon/cannons/25mm_gau12` | on_shot, building_density, Distance |
| `event:/infantry/weapon/cannons/25mm_gau12_ai` | Event Cone Angle, headphones, building_density, Direction, isPlayerIndoor, Distance, on_shot |
| `event:/infantry/weapon/cannons/25mm_gau12_interior` | on_shot |
| `event:/infantry/weapon/cannons/25mm_gau12_rotor` | Event Cone Angle, building_density, Distance, on_shot |
| `event:/infantry/weapon/cannons/25mm_gau12_rotor_ai` | Distance, on_shot |
| `event:/infantry/weapon/cannons/25mm_gau12_rotor_interior` | on_shot, Distance |
| `event:/infantry/weapon/cannons/30mm_2a38` | on_shot, Distance, building_density |
| `event:/infantry/weapon/cannons/30mm_2a38_ai` | Event Cone Angle, headphones, building_density, Direction, isPlayerIndoor, Distance, on_shot |
| `event:/infantry/weapon/cannons/30mm_2a38_interior` | on_shot |
| `event:/infantry/weapon/mguns/12mm_m2` | building_density, Distance, on_shot |
| `event:/infantry/weapon/mguns/12mm_m2_ai` | guns, headphones, building_density, isPlayerIndoor, Distance, Direction, on_shot |
| `event:/infantry/weapon/mguns/12mm_m2_interior` | on_shot |
| `event:/infantry/weapon/mguns/13mm_nsvt` | Distance, building_density, on_shot |
| `event:/infantry/weapon/mguns/13mm_nsvt_ai` | building_density, on_shot, Direction, Distance, isPlayerIndoor, guns, headphones |
| `event:/infantry/weapon/mguns/13mm_nsvt_interior` | on_shot |
| `event:/infantry/weapon/mguns/8mm_m240` | Distance, building_density, on_shot |
| `event:/infantry/weapon/mguns/8mm_m240_ai` | building_density, Distance, on_shot, Direction, isPlayerIndoor, guns, headphones |
| `event:/infantry/weapon/mguns/8mm_m240_interior` | on_shot |
| `event:/infantry/weapon/mguns/8mm_pkt` | on_shot, building_density, Distance |
| `event:/infantry/weapon/mguns/8mm_pkt_ai` | guns, headphones, building_density, isPlayerIndoor, Distance, on_shot, Direction |
| `event:/infantry/weapon/mguns/8mm_pkt_interior` | on_shot |
| `event:/infantry/weapon/rockets/75mm_m3` | Event Cone Angle, on_shot, building_density, Distance |
| `event:/infantry/weapon/rockets/75mm_m3_ai` | isPlayerIndoor, Distance, on_shot, Direction, building_density, headphones |
| `event:/infantry/weapon/rockets/75mm_m3_interior` | Distance, on_shot |

## infantry_weapon_foley

2686 events (2686 named), 1839 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/common/knife/close` | occlusion |
| `event:/infantry/enemy/walker/mc_soldier/foley_mov/common/knife/open` | occlusion |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun1_burst` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun1_shot` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun1_tail` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun2_burst` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun2_shot` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun2_tail` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun3_burst` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun3_shot` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun3_tail` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun4_burst` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun4_shot` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun4_tail` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun5_burst` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun5_shot` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun5_tail` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun6_burst` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun6_shot` |  |
| `event:/infantry/enemy/weapon/_common/far_mgun/far_mgun6_tail` |  |
| `event:/infantry/enemy/weapon/_common/tail_mgun` |  |
| `event:/infantry/enemy/weapon/_common/tail_mgun_add` |  |
| `event:/infantry/enemy/weapon/_common/tail_mgun_far` |  |
| `event:/infantry/enemy/weapon/_common/tail_pistol` |  |
| `event:/infantry/enemy/weapon/_common/tail_pistol_add` |  |
| `event:/infantry/enemy/weapon/_common/tail_pistol_far` |  |
| `event:/infantry/enemy/weapon/_common/tail_rifle` |  |
| `event:/infantry/enemy/weapon/_common/tail_rifle_add` |  |
| `event:/infantry/enemy/weapon/_common/tail_rifle_far` |  |
| `event:/infantry/enemy/weapon/_common/tail_sniper_rifle_far` |  |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_belt_out` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_belt_rattle` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_shell_second_in` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/_mc_reloadings/reload_vog_in` | occlusion |
| `event:/infantry/enemy/weapon/_reloadings/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/_reloadings/reload_belt_out` | occlusion |
| `event:/infantry/enemy/weapon/_reloadings/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/_reloadings/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/_reloadings/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/_reloadings/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/_reloadings/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/_reloadings/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/_reloadings/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/_reloadings/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/_reloadings/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/_reloadings/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/_antivehicle_template/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/_antivehicle_template/reload_shell_in_add` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/_antivehicle_template/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/_antivehicle_template/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/atr_boys/bolt_action` |  |
| `event:/infantry/enemy/weapon/antivehicle/atr_boys/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/atr_boys/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/atr_boys/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/atr_boys/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/fim_92a_stinger/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/fim_92a_stinger/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/fim_92a_stinger/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/fim_92a_stinger/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/gp_34/mod_reload` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/grb_39/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/grb_39/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/grb_39/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/grb_39/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/igla/pzrk_target_active` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/igla/pzrk_target_locked` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/igla/pzrk_target_prepare` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/javelin/reload_attach` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/javelin/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/javelin/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/javelin/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/luftfaust_b/reload` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/m136_at4/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/m136_at4/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/m136_at4/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/m136_at4/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/m136_at4/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/m1_bazooka/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/m1_bazooka/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/m1_bazooka/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/m203/mod_activate` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/m203/mod_deactivate` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/m203/mod_reload` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/mortar_2b25/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/mortar_rm_40/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/mortar_rm_40/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/mortar_rm_40/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/mortyr_grenade_launcher/mod_activate` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/mortyr_grenade_launcher/mod_deactivate` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/mortyr_grenade_launcher/mod_reload` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/mpads_verba/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/mpads_verba/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/mpads_verba/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/mpads_verba/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/neiman_minethrower/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/neiman_minethrower/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/neiman_minethrower/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/neiman_minethrower/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/panzerfaust_100/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/panzerfaust_100/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/panzerfaust_100/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/panzerschreck/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/panzerschreck/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/panzerschreck/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/piat/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/piat/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/piat/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/ptrs41/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/ptrs41/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/ptrs41/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/pzb39/bolt_action_1` |  |
| `event:/infantry/enemy/weapon/antivehicle/pzb39/bolt_action_2` |  |
| `event:/infantry/enemy/weapon/antivehicle/pzb39/bolt_action_3` |  |
| `event:/infantry/enemy/weapon/antivehicle/pzb39/bolt_action_4` |  |
| `event:/infantry/enemy/weapon/antivehicle/pzb39/bolt_action_5` |  |
| `event:/infantry/enemy/weapon/antivehicle/pzb39/bolt_action_6` |  |
| `event:/infantry/enemy/weapon/antivehicle/pzb39/bolt_action_7` |  |
| `event:/infantry/enemy/weapon/antivehicle/pzb39/bolt_action_8` |  |
| `event:/infantry/enemy/weapon/antivehicle/pzb39/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/pzb39/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/pzb39/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/pzb39/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/rpg_7/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/rpg_7/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/rpg_7/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/rpg_7/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/rpg_7/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/rpzb_43/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/rpzb_43/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/rpzb_43/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/type_5_rocket_launcher/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/type_5_rocket_launcher/reload_shell_in_add` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/type_5_rocket_launcher/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/type_5_rocket_launcher/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/type_97_antitank/reload` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/type_97_antitank/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/vpgs_grenade_launcher/mod_activate` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/vpgs_grenade_launcher/mod_deactivate` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/vpgs_grenade_launcher/mod_reload` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/wz_35/bolt_action` |  |
| `event:/infantry/enemy/weapon/antivehicle/wz_35/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/wz_35/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/wz_35/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/antivehicle/wz_35/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/explosive/activate` |  |
| `event:/infantry/enemy/weapon/explosive/throw` |  |
| `event:/infantry/enemy/weapon/grenade/activate` | occlusion |
| `event:/infantry/enemy/weapon/grenade/activate_with_clap` | occlusion, Distance |
| `event:/infantry/enemy/weapon/grenade/throw` | occlusion |
| `event:/infantry/enemy/weapon/grenade_flash/activate` |  |
| `event:/infantry/enemy/weapon/grenade_flash/throw` |  |
| `event:/infantry/enemy/weapon/incendiary_grenade/activate` |  |
| `event:/infantry/enemy/weapon/melee/aspen_stake/whoosh` |  |
| `event:/infantry/enemy/weapon/melee/axe/whoosh` |  |
| `event:/infantry/enemy/weapon/melee/bat/whoosh` |  |
| `event:/infantry/enemy/weapon/melee/hands/whoosh` | Distance |
| `event:/infantry/enemy/weapon/melee/knife/whoosh` |  |
| `event:/infantry/enemy/weapon/melee/lunge_mine/whoosh` |  |
| `event:/infantry/enemy/weapon/melee/machete/whoosh` |  |
| `event:/infantry/enemy/weapon/melee/mgun/whoosh` |  |
| `event:/infantry/enemy/weapon/melee/pipe/whoosh` |  |
| `event:/infantry/enemy/weapon/melee/pistol/whoosh` |  |
| `event:/infantry/enemy/weapon/melee/rifle/whoosh` |  |
| `event:/infantry/enemy/weapon/melee/shovel/whoosh` | Distance |
| `event:/infantry/enemy/weapon/melee/sword/whoosh` |  |
| `event:/infantry/enemy/weapon/mgun/ab_46/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ab_46/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ab_46/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ab_46/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ab_46/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_103/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_103/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_103/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_12/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_12/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_12/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_12/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_12/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_12/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_47/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_47/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_47/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_47/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_47/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_74/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_74/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_74/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_74/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ak_74/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/akm/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/akm/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/akm/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/akm/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/akm/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_94/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_94/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_94/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_94/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_94/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_m2_stinger/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_m2_stinger/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_m2_stinger/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_m2_stinger/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_m2_stinger/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_m2_stinger/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_m2_stinger/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_m2_stinger/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_m2_stinger/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/an_m2_stinger/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/as_44/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/as_44/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/as_44/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/as_val/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/as_val/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/as_val/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/as_val/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/as_val/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/as_val/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/at_44/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/at_44/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/at_44/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/at_44/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/avs36/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/avs36/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/avs36/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/beretta_m1918/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/beretta_m1918/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/beretta_m1918/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/besal_lmg/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/besal_lmg/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/besal_lmg/reload6/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/besal_lmg/reload7/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/breda_mod_30/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/breda_mod_30/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/bren_100_round_drum/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/bren_100_round_drum/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/bren_100_round_drum/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/bren_100_round_drum/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/bren_100_round_drum/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/bren_100_round_drum/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/bren_100_round_drum/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/bren_100_round_drum/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/charlton/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/charlton/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/chatellerault_m_24_29/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/chatellerault_m_24_29/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/chatellerault_m_24_29/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/chatellerault_m_24_29/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/chatellerault_m_24_29/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/chauchat/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/chauchat/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/chauchat/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/chauchat/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/chauchat/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/coenders_mp/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/coenders_mp/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/coenders_smg/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/coenders_smg/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/colt_9_mm_smg/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/colt_9_mm_smg/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/colt_9_mm_smg/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/colt_9_mm_smg/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/colt_9_mm_smg/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/cz_bren_2/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/cz_bren_2/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/cz_bren_2/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/danuvia_43m/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/danuvia_43m/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/danuvia_43m/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dp27/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dp27/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dp27/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dp27/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dp27/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dp27/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dp27/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dp_42_beltfed/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dp_42_beltfed/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dpm/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dpm/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dpm/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dpm/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/dpm/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/erma_emp/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/erma_emp/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/erma_emp/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fedorov/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fedorov/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fedorov/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fg42/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fg42/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fg42/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fg42_m2/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fg42_m2/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fg42_m2/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fn_m1930/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fn_m1930/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fn_scar_h/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fn_scar_h/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fn_scar_h/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fnab_43/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fnab_43/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/fnab_43/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/gorov_mg/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/gorov_mg/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hk_mp5/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hk_mp5/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hk_mp5/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hk_mp5/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hk_mp7a2/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hk_mp7a2/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hk_mp7a2/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hk_mp7a2/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hk_mp7a2/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hk_mp7a2/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/horn_sturmgewehr/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/horn_sturmgewehr/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/horn_sturmgewehr/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hotchkiss_m1922/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hotchkiss_m1922/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hotchkiss_m1922/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hotchkiss_m1922/reload_mag_in_add` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hotchkiss_m1922/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hotchkiss_m1922/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hotchkiss_m1922/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hotchkiss_m1922/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hotchkiss_m1922/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hyde_model_35_gun/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hyde_model_35_gun/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/hyde_model_35_gun/reload_dual` | occlusion |
| `event:/infantry/enemy/weapon/mgun/knorr_bremse_mg_35_36/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/knorr_bremse_mg_35_36/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/knorr_bremse_mg_35_36/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/knorr_bremse_mg_35_36/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/knorr_bremse_mg_35_36/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/knorr_bremse_mg_35_36/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/krieghoff_fg/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/krieghoff_fg/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/krieghoff_fg/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/kriss_vector/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/kriss_vector/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/kriss_vector/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/kriss_vector/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/kriss_vector/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/kriss_vector/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/kriss_vector/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lad/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lad/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lahti_saloranta_m26/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lahti_saloranta_m26/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lahti_saloranta_m26/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lahti_saloranta_m26/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lahti_saloranta_m26/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lahti_saloranta_m26/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lahti_saloranta_m26/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lanchester_model_1/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lanchester_model_1/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lewis/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lewis/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lewis/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lewis/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/lewis/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m16a4/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m16a4/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m16a4/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m16a4/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m16a4/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1918/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1918/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1918/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1918/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1919a6/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1919a6/reload_belt_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1919a6/reload_belt_rattle` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1919a6/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1919a6/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1919a6/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1919a6/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1919a6/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1919a6/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1919a6/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m1919a6/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m240/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m240/reload_belt_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m240/reload_belt_rattle` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m240/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m240/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m240/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m240/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m240/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m240/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m240/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m240/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m249/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m249/reload_belt_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m249/reload_belt_rattle` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m249/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m249/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m249/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m249/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m249/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m249/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m249/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m249/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m27_iar/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m27_iar/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m27_iar/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m27_iar/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m27_iar/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m3/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m3/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m3/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m3/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m38/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m38/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m38/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m4/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m4/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m4/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m4a1/reload_drum_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m4a1/reload_drum_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m4a1/reload_drum_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m4a1/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m4a1/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m4a1/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m4a1/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m4a1/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m50/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m50/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m50/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/m50/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mac_11/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mac_11/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mac_11/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mac_11/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mac_11/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mac_11/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mac_11/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mac_11/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mac_11/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/madsen/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/madsen/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/maxim_tokarev/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/maxim_tokarev/reload_belt_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/maxim_tokarev/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/maxim_tokarev/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/maxim_tokarev/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/maxim_tokarev/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/maxim_tokarev/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg42/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg42/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg42/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg42/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg42/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg42/reload6/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg42/reload7/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg42/reload8/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_13/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_13/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_13/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_13/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_13/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_13/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_13/reload6/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_13/reload7/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_13/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_15/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_15/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_15/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_15/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_15/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_15/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_15/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_30/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_30/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_34/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_34/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_34/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_34/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_34/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_34/reload6/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_34/reload7/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_34_patronentrommel/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_34_patronentrommel/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_42_beltfed/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_42_beltfed/reload_belt_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_42_beltfed/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_42_beltfed/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_42_beltfed/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_42_beltfed/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_42_beltfed/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_42_beltfed/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_81_infantry/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_81_infantry/reload_belt_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_81_infantry/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_81_infantry/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_81_infantry/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_81_infantry/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mg_81_infantry/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mk_48/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mk_48/reload_belt_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mk_48/reload_belt_rattle` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mk_48/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mk_48/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mk_48/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mk_48/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mk_48/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mk_48/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mk_48/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mk_48/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mkb_42_w/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mkb_42_w/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mkb_42_w/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp18/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp18/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp18/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp34o/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp34o/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp34o/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp35/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp35/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp35/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp40/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp40/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp40/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/mp40/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/nambu_type_1_early_smg/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/nambu_type_1_early_smg/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/nambu_type_1_smg/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/nambu_type_1_smg/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/nambu_type_2a_smg/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/nambu_type_2a_smg/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/nambu_type_99_lmg/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/nambu_type_99_lmg/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pkp_pecheneg/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pkp_pecheneg/reload_belt_rattle` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pkp_pecheneg/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pkp_pecheneg/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pkp_pecheneg/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pkp_pecheneg/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pkp_pecheneg/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pkp_pecheneg/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pkp_pecheneg/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pkp_pecheneg/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_bizon/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_bizon/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_bizon/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_bizon/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_bizon/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_bizon/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_bizon/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_bizon/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_vityaz/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_vityaz/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_vityaz/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_vityaz/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_vityaz/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_19_vityaz/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_2000/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_2000/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_2000/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_2000/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_2000/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_2000/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_2000/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_2000/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_71/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_71/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_71/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_71/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_71/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_71/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_71/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_71/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_dolganov/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_dolganov/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_dolganov/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pp_dolganov/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppd3438/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppd3438/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppd3438/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppd3438_box/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppd3438_box/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppd3438_box/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppd40/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppd40/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppd40/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppk_41/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppk_41/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppk_41/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pps_42/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pps_42/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/pps_42/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppsh/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppsh/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppsh/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppsh/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppsh_40/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ppsh_40/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rd_44/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rd_44/reload_belt_rattle` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rd_44/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rd_44/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rd_44/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rd_44/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rd_44/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rd_44/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rd_44/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rp_46/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rp_46/reload_belt_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rp_46/reload_belt_rattle` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rp_46/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rp_46/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rp_46/reload_mag_latch_lock` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rp_46/reload_mag_latch_unlock` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rp_46/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rp_46/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rp_46/reload_shutter` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_16/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_16/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_16/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_16/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_16/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_1943/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_1943/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_1943/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_1943/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_1943/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_1943/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_74m/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_74m/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_74m/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_74m/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/rpk_74m/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/schmeisser_mk36/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/schmeisser_mk36/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/schmeisser_mk36/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/scorpion_evo_3/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/scorpion_evo_3/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/scorpion_evo_3/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/scorpion_evo_3/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/scorpion_evo_3/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/scorpion_evo_3/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/scorpion_evo_3/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_1920/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_1920/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_1920/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_ke_7/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_ke_7/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_ke_7/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_ke_7/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/reload_belt_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/reload_belt_rattle` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm250/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm5/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm5/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm5/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm5/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm5/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm5/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sig_xm5/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sten_mk2/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sten_mk2/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/sten_mk2/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/steyr_aug/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/steyr_aug/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/steyr_aug/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/stg_44/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/stg_44/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/stg_44/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/stg_44/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/suomi_kp_31/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/suomi_kp_31/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/suomi_kp_31/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/t24_mg/reload_belt_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/t24_mg/reload_belt_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/t24_mg/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/t24_mg/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/t24_mg/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/t24_mg/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/t24_mg/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/t24_mg/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_100_drum/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_100_drum/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_100_drum/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_100_drum/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_m1921ac/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_m1921ac/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_m1921ac/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_m1921ac/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_m1921ac/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_m1921ac/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_m1928a1_50_drum/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/thompson_m1928a1_50_drum/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/tokyo_arsenal_model_1927/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/tokyo_arsenal_model_1927/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/tokyo_arsenal_model_1927/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/tokyo_arsenal_model_1927/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/type_100_mg/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/type_100_mg/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/type_100_mg/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/mgun/type_100_mg/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/type_100_mg/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/type_100_mg/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/type_100_smg/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/type_100_smg/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ud_m42/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/ud_m42/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mgun/vollmer_m35/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/vollmer_m35/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/vollmer_m35/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/yazikov_smg/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/mgun/yazikov_smg/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/mgun/yazikov_smg/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/yazikov_smg/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/mgun/yazikov_smg/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/mgun/zb_26/reload` | occlusion |
| `event:/infantry/enemy/weapon/mgun/zb_26/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/zb_26/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/zb_26/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/zb_26/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/zb_26/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/zb_26/reload6/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/zb_26/reload7/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/mgun/zb_26/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/mine/activate` |  |
| `event:/infantry/enemy/weapon/mine/drop` | Distance |
| `event:/infantry/enemy/weapon/mine/throw` |  |
| `event:/infantry/enemy/weapon/misc/flamethrower/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/misc/flamethrower/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/misc/flamethrower/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/molotov/activate` |  |
| `event:/infantry/enemy/weapon/molotov/throw` |  |
| `event:/infantry/enemy/weapon/pistol/_pistol_template/mag_in` | occlusion |
| `event:/infantry/enemy/weapon/pistol/_pistol_template/mag_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/_pistol_template/shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/pistol/_pistol_template/shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/beretta_m1923/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/beretta_m9/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/pistol/beretta_m9/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/pistol/beretta_m9/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/pistol/beretta_m9/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/beretta_m9/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/pistol/beretta_m9/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/c96/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/c96/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/c96/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/c96_m712/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/c96_m712/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/c96_m712/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/colt_new_service/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/colt_new_service/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/colt_new_service/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/dreyse_m1907/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/dreyse_m1907/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/dreyse_m1907/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/m1911/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/m1911/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/m1911/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/m45a1_cqbp/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/pistol/m45a1_cqbp/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/pistol/m45a1_cqbp/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/pistol/m45a1_cqbp/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/m45a1_cqbp/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/pistol/m45a1_cqbp/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/m45a1_cqbp/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/makarov/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/pistol/makarov/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/pistol/makarov/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/pistol/makarov/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/makarov/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/pistol/makarov/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/makarov/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/mp_443/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/pistol/mp_443/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/pistol/mp_443/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/pistol/mp_443/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/mp_443/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/pistol/mp_443/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/mp_443/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/pistol/mp_443/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/nagant_1895/bolt_action` |  |
| `event:/infantry/enemy/weapon/pistol/nagant_1895/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/nagant_1895/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/nagant_1895/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/p08/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/p08/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/p08/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/p08/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/p38/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/p38/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/p38/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/sturmpistole/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/sturmpistole/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/sturmpistole/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/sturmpistole/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/sturmpistole/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/sturmpistole/reload6/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/sturmpistole/reload7/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/sw_m1917/bolt_action` |  |
| `event:/infantry/enemy/weapon/pistol/tk_26/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/tk_26/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/tk_26/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/tt/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/tt/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/tt/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/voevodin_pistol/reload` | occlusion |
| `event:/infantry/enemy/weapon/pistol/voevodin_pistol/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/pistol/walther_pp/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/walther_pp/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/walther_pp/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/pistol/welrod_mk2/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/pistol/welrod_mk2/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/pistol/welrod_mk2/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/pistol/welrod_mk2/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/_rifle_template/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/_rifle_template/mod_activate` | occlusion |
| `event:/infantry/enemy/weapon/rifle/_rifle_template/mod_deactivate` | occlusion |
| `event:/infantry/enemy/weapon/rifle/_rifle_template/mod_reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/_rifle_template/reload_loop` | occlusion |
| `event:/infantry/enemy/weapon/rifle/_rifle_template/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/_rifle_template/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_38/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_38/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_38/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_38/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_38/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_38/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_38/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_early_short/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_early_short/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_early_short/reload_loop` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_early_short/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_early_short/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_early_sniper/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_early_sniper/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_early_sniper/reload_loop` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_early_sniper/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_early_sniper/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_late/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_late/reload` | mat, occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_late/reload_loop` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_late/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/arisaka_type_99_late/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/armaguerra_mod_39/ammo_eject` | occlusion |
| `event:/infantry/enemy/weapon/rifle/armaguerra_mod_39/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/armaguerra_mod_39/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/armaguerra_mod_39/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/armaguerra_mod_39/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/armaguerra_mod_39/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/avt_40/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/avt_40/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/avt_40/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/barrett_m82a1/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/barrett_m82a1/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/barrett_m82a1/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/barrett_m82a1/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/barrett_m82a1/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/barrett_m82a1/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/barrett_m82a1/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/barrett_m82a1/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/rifle/barrett_m82a1/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/barrett_m82a1/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/beretta_m31/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/beretta_m31/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/beretta_m31/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/beretta_m31/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/beretta_m31/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/berthier_m16/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/berthier_m16/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/berthier_m16/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/rifle/breda_m1935_pg/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/breda_m1935_pg/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/rifle/browning_auto_5/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/browning_auto_5/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/browning_auto_5/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/carcano_m41/ammo_eject` | occlusion |
| `event:/infantry/enemy/weapon/rifle/carcano_m41/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/carcano_m41/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/carcano_m41/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/carcano_m41/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/carcano_m41/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/delisle_commando_carbine/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/delisle_commando_carbine/reload3` | occlusion |
| `event:/infantry/enemy/weapon/rifle/delisle_commando_carbine/reload4` | occlusion |
| `event:/infantry/enemy/weapon/rifle/dp_12/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/dp_12/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/dp_12/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/dp_12/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/dp_12/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/farquhar_hill_1918/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/farquhar_hill_1918/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/rifle/fedorov_rifle_5_rounds/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/fedorov_rifle_5_rounds/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/fedorov_rifle_5_rounds/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/fedorov_rifle_5_rounds/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/fedorov_rifle_5_rounds/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/fedorov_rifle_5_rounds/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/fedorov_rifle_5_rounds/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr41/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/gewehr41/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr41/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr41/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr41/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr41/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr41/reload_loop_multiple` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr41/reload_loop_single` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr41/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr41/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr43/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/gewehr43/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr43/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr43/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr43/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/gewehr_88/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/hino_komuro_m1904/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/hino_komuro_m1904/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/hino_komuro_m1904/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/hino_komuro_m1904/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/hino_komuro_m1904/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/rifle/hino_komuro_m1904/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/hk_g3a4/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/hk_g3a4/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/hk_g3a4/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/hk_g3a4/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/hk_g3a4/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/hk_g3a4/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ithaca_37/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/ithaca_37/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ithaca_37/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ithaca_37/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/kar98k_kriegsmodell/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/kar98k_kriegsmodell/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/kar98k_kriegsmodell/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/kar98k_kriegsmodell/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/kar98k_kriegsmodell/reload6/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/koko_rifle/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/koko_rifle/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/koko_rifle/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/koko_rifle/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/koko_rifle/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/koko_rifle/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/koko_rifle/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ks_p_18_5/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ks_p_18_5/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ks_p_18_5/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ks_p_18_5/reload_shell_second_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ksvk_12_7/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/ksvk_12_7/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ksvk_12_7/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ksvk_12_7/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lebel_1886_m93/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/lebel_1886_m93/reload_loop` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lebel_1886_m93/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lebel_1886_m93/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lee_enfield/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/lee_enfield/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lee_enfield/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lee_enfield/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lee_enfield/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lee_enfield/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lee_enfield/reload_loop_multiple` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lee_enfield/reload_loop_single` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lee_enfield/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lee_enfield/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/liu_rifle/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/liu_rifle/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/liu_rifle/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/liu_rifle/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/liu_rifle/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/liu_rifle/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/liu_rifle/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lw_3/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lw_3/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/lw_3/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1/ammo_eject` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/m1/mod_activate` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1/mod_deactivate` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1/mod_reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m110a1_sdmr/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m110a1_sdmr/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m110a1_sdmr/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m110a1_sdmr/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m110a1_sdmr/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m110a1_sdmr/reload_mag_punch_2` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1903/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/m1903/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1903/reload_loop` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1903/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1903/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1903_pedersen/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1903_pedersen/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1903_springfield/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/m1903_springfield/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1903_springfield/reload_loop_multiple` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1903_springfield/reload_loop_single` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1903_springfield/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1903_springfield/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1917_enfield/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/m1917_enfield/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1917_enfield/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1917_enfield/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1917_enfield/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1917_enfield/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1917_enfield/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1941_johnson/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/m1941_johnson/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1941_johnson/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1941_johnson/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1941_johnson/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1941_johnson/reload_loop_multiple` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1941_johnson/reload_loop_single` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1941_johnson/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1941_johnson/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1a1_carbine/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1a1_carbine/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m1a1_carbine/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m24/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/m24/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m24/reload_loop` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m24/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m24/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m30_luftwaffe/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m30_luftwaffe/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m30_luftwaffe/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m30_luftwaffe/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/m30_luftwaffe/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mannlicher_m1895/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/mannlicher_m1895/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mannlicher_m1895/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mannlicher_m1895/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mannlicher_m1895/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mannlicher_m93_roman/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/mannlicher_m93_roman/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mannlicher_m93_roman/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mas_36/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/mas_36/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mas_36/reload_loop` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mas_36/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mas_36/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser98k/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/mauser98k/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser98k/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser98k/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser98k/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser98k/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser98k/reload6/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser98k/reload7/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser98k/reload_loop_multiple` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser98k/reload_loop_single` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser98k/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser98k/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser_gewehr_98_warmod/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/mauser_gewehr_98_warmod/reload_loop_multiple` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser_gewehr_98_warmod/reload_loop_single` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser_gewehr_98_warmod/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mauser_gewehr_98_warmod/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mcmillan_tac_50/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mcmillan_tac_50/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mcmillan_tac_50/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mcmillan_tac_50/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mcmillan_tac_50/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mcmillan_tac_50/reload_shell_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mcmillan_tac_50/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mcmillan_tac_50/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/meunier_a6_carbine/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/meunier_a6_carbine/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/meunier_a6_carbine/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/meunier_a6_carbine/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/meunier_a6_carbine/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/meunier_a6_carbine/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/meunier_a6_carbine/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/meunier_a6_carbine/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mk_14_ebr/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mk_14_ebr/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mk_14_ebr/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mk_14_ebr/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mk_14_ebr/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mondragon/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mondragon/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/mosin/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin/reload_clip_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin/reload_loop` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin_1928/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mosin_m1907/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mossberg_590/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mossberg_590/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mossberg_590/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mossberg_590/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/mossberg_590/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/pavesi_m42/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/pavesi_m42/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/pavesi_m42/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/pavesi_m42/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/pavesi_m42/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/pavesi_prototype_svt_copy/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/pavesi_prototype_svt_copy/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/pavesi_prototype_svt_copy/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/pavesi_prototype_svt_copy/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/pavesi_prototype_svt_copy/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/pavesi_prototype_svt_copy/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/pavesi_prototype_svt_copy/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/remington_870/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/remington_870/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/remington_870/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/remington_870/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/remington_870/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ross_rifle/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/ross_rifle/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ross_rifle/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ross_rifle/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ross_rifle/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ross_rifle/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ross_rifle/reload_loop` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ross_rifle/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/ross_rifle/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_30/reload_clip_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_30/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_30/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_30/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_30/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_30/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_30/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_30/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_30/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_31/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_31/reload_loop` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_31/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sks_31/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/spas_12/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/spas_12/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/spas_12/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/spas_12/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/stl_mosin_m91_30/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sv_98/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sv_98/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sv_98/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sv_98/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sv_98/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sv_98/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svch/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svch/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svch/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svch/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svch/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svd_m/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svd_m/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svd_m/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svd_m/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svd_m/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svt40/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/svt40/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svt40/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svt40/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svt40/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svt40/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/svt40/reload6/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/sw_light_rifle/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/t20_early_rifle/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/t20_early_rifle/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/t20_early_rifle/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/t20_early_rifle/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/t20_rifle/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/t20_rifle/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/rifle/turner/reload_loop_multiple` | occlusion |
| `event:/infantry/enemy/weapon/rifle/turner/reload_loop_single` | occlusion |
| `event:/infantry/enemy/weapon/rifle/turner/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/turner/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_22_murata/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_22_murata/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_22_murata/reload_mag_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_22_murata/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_22_murata/reload_shell_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_22_murata/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_22_murata/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_4/reload_loop_multiple` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_4/reload_loop_single` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_4/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_4/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_hei/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_hei/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_hei_automatic_rifle/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_hei_automatic_rifle/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_hei_automatic_rifle/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_hei_automatic_rifle/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_hei_automatic_rifle/reload_mag_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_hei_automatic_rifle/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_hei_extended/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_hei_extended/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_hei_late/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_hei_late/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_i/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/type_i/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_ko_rifle/reload_loop_multiple` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_ko_rifle/reload_loop_single` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_ko_rifle/reload_post` | occlusion |
| `event:/infantry/enemy/weapon/rifle/type_ko_rifle/reload_prepare` | occlusion |
| `event:/infantry/enemy/weapon/rifle/vintorez/reload_foley_end` | occlusion |
| `event:/infantry/enemy/weapon/rifle/vintorez/reload_foley_start` | occlusion |
| `event:/infantry/enemy/weapon/rifle/vintorez/reload_mag_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/vintorez/reload_mag_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/vintorez/reload_shutter_in` | occlusion |
| `event:/infantry/enemy/weapon/rifle/vintorez/reload_shutter_out` | occlusion |
| `event:/infantry/enemy/weapon/rifle/vstg_1_5/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/vstg_1_5/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/vstg_1_5/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/winchester_1895/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/winchester_1895/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/winchester_1895/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/winchester_1895/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/winchester_1895/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/winchester_1895/reload5/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/winchester_1912/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/winchester_1912/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/winchester_1912/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/winchester_1912/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/winchester_m1907/reload_mag_punch` | occlusion |
| `event:/infantry/enemy/weapon/rifle/zh_29/bolt_action` |  |
| `event:/infantry/enemy/weapon/rifle/zh_29/reload1/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/zh_29/reload2/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/zh_29/reload3/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/zh_29/reload4/change_ammo` | occlusion |
| `event:/infantry/enemy/weapon/rifle/zh_29_jp/reload` | occlusion |
| `event:/infantry/enemy/weapon/rifle/zh_29_jp/reload_alt` | occlusion |
| `event:/infantry/enemy/weapon/tnt_block_exploder/activate` |  |
| `event:/infantry/player/weapon/_common/ammo_box_drop` | mat |
| `event:/infantry/player/weapon/_common/change_mode` |  |
| `event:/infantry/player/weapon/_common/clip_drop` | mat |
| `event:/infantry/player/weapon/_common/drum_drop` | mat |
| `event:/infantry/player/weapon/_common/magazine_drop` | mat |
| `event:/infantry/player/weapon/_common/pistol_magazine_drop` | mat |
| `event:/infantry/player/weapon/_common/rigid_belt_drop` | mat |
| `event:/infantry/player/weapon/_common/shell_drop` | mat |
| `event:/infantry/player/weapon/_common/shell_mid_drop_in_tank` | mat |
| `event:/infantry/player/weapon/_common/shell_out` | mat |
| `event:/infantry/player/weapon/_common/shell_out_in_tank` | mat |
| `event:/infantry/player/weapon/_common/shell_out_in_tank_loop` | mat |
| `event:/infantry/player/weapon/_common/shell_out_loop` | mat |
| `event:/infantry/player/weapon/_common/shotgun_shell_out` | mat |
| `event:/infantry/player/weapon/_common/tail_mgun` |  |
| `event:/infantry/player/weapon/_common/vog_off` |  |
| `event:/infantry/player/weapon/_common/vog_on` |  |
| `event:/infantry/player/weapon/_common/zoom` |  |
| `event:/infantry/player/weapon/_mc_common/shell_mid_drop_in_tank` | mat |
| `event:/infantry/player/weapon/_mc_common/shell_small_drop_in_tank` | mat |
| `event:/infantry/player/weapon/_mc_reloadings/cloth/cloth_end` |  |
| `event:/infantry/player/weapon/_mc_reloadings/cloth/cloth_mag_in` |  |
| `event:/infantry/player/weapon/_mc_reloadings/cloth/cloth_mag_out` |  |
| `event:/infantry/player/weapon/_mc_reloadings/cloth/cloth_mag_take` |  |
| `event:/infantry/player/weapon/_mc_reloadings/cloth/cloth_shutter_in` |  |
| `event:/infantry/player/weapon/_mc_reloadings/cloth/cloth_shutter_out` |  |
| `event:/infantry/player/weapon/_mc_reloadings/cloth/cloth_start` |  |
| `event:/infantry/player/weapon/_mc_reloadings/rattles/rattl_end` |  |
| `event:/infantry/player/weapon/_mc_reloadings/rattles/rattl_mag_in` |  |
| `event:/infantry/player/weapon/_mc_reloadings/rattles/rattl_mag_out` |  |
| `event:/infantry/player/weapon/_mc_reloadings/rattles/rattl_mag_take` |  |
| `event:/infantry/player/weapon/_mc_reloadings/rattles/rattl_shutter_in` |  |
| `event:/infantry/player/weapon/_mc_reloadings/rattles/rattl_shutter_out` |  |
| `event:/infantry/player/weapon/_mc_reloadings/rattles/rattl_start` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_belt_in` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_belt_out` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_belt_rattle` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_foley_end` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_foley_start` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_mag_in` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_mag_out` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_mag_punch` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_shell_in` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_shutter_in` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_shutter_out` |  |
| `event:/infantry/player/weapon/_mc_reloadings/reload_vog_in` |  |
| `event:/infantry/player/weapon/_reloadings/belt_in/belt_in_lmg4` |  |
| `event:/infantry/player/weapon/_reloadings/belt_out/belt_out_lmg4` |  |
| `event:/infantry/player/weapon/_reloadings/clip_out/clip_out_rifle_bolt` |  |
| `event:/infantry/player/weapon/_reloadings/clip_out/clip_out_rifle_bolt2` |  |
| `event:/infantry/player/weapon/_reloadings/clip_out/clip_out_rifle_bolt3` |  |
| `event:/infantry/player/weapon/_reloadings/clip_out/clip_out_rifle_bolt4` |  |
| `event:/infantry/player/weapon/_reloadings/clip_out/clip_out_rifle_bolt5` |  |
| `event:/infantry/player/weapon/_reloadings/clip_out/clip_out_semi` |  |
| `event:/infantry/player/weapon/_reloadings/clip_out/clip_out_semi4` |  |
| `event:/infantry/player/weapon/_reloadings/cloth/cloth_end` |  |
| `event:/infantry/player/weapon/_reloadings/cloth/cloth_mag_in` |  |
| `event:/infantry/player/weapon/_reloadings/cloth/cloth_mag_out` |  |
| `event:/infantry/player/weapon/_reloadings/cloth/cloth_mag_take` |  |
| `event:/infantry/player/weapon/_reloadings/cloth/cloth_shutter_in` |  |
| `event:/infantry/player/weapon/_reloadings/cloth/cloth_shutter_out` |  |
| `event:/infantry/player/weapon/_reloadings/cock_trigger/cock_trigger` |  |
| `event:/infantry/player/weapon/_reloadings/cock_trigger/cock_trigger2` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_drum` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_drum1` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_lmg` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_lmg2` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_lmg3` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_lmg4` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_lmg5` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_pt` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_pt1` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_ptr` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_rifle_bolt` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_rifle_bolt3` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_rifle_bolt4` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_rifle_bolt5` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_semi` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_semi1` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_semi2` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_semi3` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_semi4` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_smg1` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_smg2` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_smg3` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_smg4` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_smg5` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_smg_plastic` |  |
| `event:/infantry/player/weapon/_reloadings/mag_in/mag_in_ubgl` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_drum` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_drum1` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_lmg` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_lmg2` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_lmg3` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_lmg4` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_lmg5` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_pt` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_pt1` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_ptr` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_semi` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_semi1` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_semi2` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_smg1` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_smg2` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_smg3` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_smg4` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_smg5` |  |
| `event:/infantry/player/weapon/_reloadings/mag_out/mag_out_smg_plastic` |  |
| `event:/infantry/player/weapon/_reloadings/mag_punch/mag_punch_drum1` |  |
| `event:/infantry/player/weapon/_reloadings/mag_punch/mag_punch_lmg2` |  |
| `event:/infantry/player/weapon/_reloadings/mag_punch/mag_punch_semi4` |  |
| `event:/infantry/player/weapon/_reloadings/mag_punch/mag_punch_smg3` |  |
| `event:/infantry/player/weapon/_reloadings/mag_shutter_in/mag_shutter_in_lmg2` |  |
| `event:/infantry/player/weapon/_reloadings/mag_shutter_in/mag_shutter_in_lmg4` |  |
| `event:/infantry/player/weapon/_reloadings/mag_shutter_in/mag_shutter_in_lmg5` |  |
| `event:/infantry/player/weapon/_reloadings/mag_shutter_in/mag_shutter_in_semi2` |  |
| `event:/infantry/player/weapon/_reloadings/mag_shutter_out/mag_shutter_out_lmg2` |  |
| `event:/infantry/player/weapon/_reloadings/mag_shutter_out/mag_shutter_out_lmg5` |  |
| `event:/infantry/player/weapon/_reloadings/mag_shutter_out/mag_shutter_out_ptr` |  |
| `event:/infantry/player/weapon/_reloadings/mag_shutter_out/mag_shutter_out_semi1` |  |
| `event:/infantry/player/weapon/_reloadings/mag_shutter_out/mag_shutter_out_semi2` |  |
| `event:/infantry/player/weapon/_reloadings/mag_shutter_out/mag_shutter_out_semi3` |  |
| `event:/infantry/player/weapon/_reloadings/mag_shutter_out/mag_shutter_out_smg3` |  |
| `event:/infantry/player/weapon/_reloadings/rattles/rattl_end` |  |
| `event:/infantry/player/weapon/_reloadings/rattles/rattl_mag_in` |  |
| `event:/infantry/player/weapon/_reloadings/rattles/rattl_mag_out` |  |
| `event:/infantry/player/weapon/_reloadings/rattles/rattl_mag_take` |  |
| `event:/infantry/player/weapon/_reloadings/rattles/rattl_shutter_in` |  |
| `event:/infantry/player/weapon/_reloadings/rattles/rattl_shutter_out` |  |
| `event:/infantry/player/weapon/_reloadings/reload_belt_in` |  |
| `event:/infantry/player/weapon/_reloadings/reload_belt_out` |  |
| `event:/infantry/player/weapon/_reloadings/reload_foley_end` |  |
| `event:/infantry/player/weapon/_reloadings/reload_foley_start` |  |
| `event:/infantry/player/weapon/_reloadings/reload_mag_in` |  |
| `event:/infantry/player/weapon/_reloadings/reload_mag_out` |  |
| `event:/infantry/player/weapon/_reloadings/reload_mag_punch` |  |
| `event:/infantry/player/weapon/_reloadings/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/_reloadings/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/_reloadings/reload_shell_in` |  |
| `event:/infantry/player/weapon/_reloadings/reload_shutter_in` |  |
| `event:/infantry/player/weapon/_reloadings/reload_shutter_out` |  |
| `event:/infantry/player/weapon/_reloadings/shell_attach/shell_attach1` |  |
| `event:/infantry/player/weapon/_reloadings/shell_attach/shell_attach2` |  |
| `event:/infantry/player/weapon/_reloadings/shell_attach/shell_attach3` |  |
| `event:/infantry/player/weapon/_reloadings/shell_detach/shell_detach1` |  |
| `event:/infantry/player/weapon/_reloadings/shell_in/shell_in_rc` |  |
| `event:/infantry/player/weapon/_reloadings/shell_in/shell_in_rifle_bolt` |  |
| `event:/infantry/player/weapon/_reloadings/shell_in/shell_in_rifle_bolt3` |  |
| `event:/infantry/player/weapon/_reloadings/shell_in/shell_in_rifle_bolt4` |  |
| `event:/infantry/player/weapon/_reloadings/shell_in_add/shell_in_add_rc` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_add/shutter_add_lmg5` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_drum1` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_lmg` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_lmg2` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_lmg3` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_lmg4` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_lmg5` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_pt1` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_ptr` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_rc` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_rifle_bolt` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_rifle_bolt1` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_rifle_bolt2` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_rifle_bolt3` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_rifle_bolt4` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_rifle_bolt5` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_semi` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_semi1` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_semi3` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_semi4` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_semi5` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_smg` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_smg1` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_smg2` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_smg3` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_smg4` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_in/shutter_in_smg5` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_lmg` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_lmg2` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_pt` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_ptr` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_rc` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_rifle_bolt` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_rifle_bolt1` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_rifle_bolt2` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_rifle_bolt3` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_rifle_bolt4` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_rifle_bolt5` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_semi` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_semi1` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_semi2` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_semi3` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_semi4` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_semi5` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_smg` |  |
| `event:/infantry/player/weapon/_reloadings/shutter_out/shutter_out_smg4` |  |
| `event:/infantry/player/weapon/antivehicle/_antivehicle_template/reload_shell_in` |  |
| `event:/infantry/player/weapon/antivehicle/_antivehicle_template/reload_shell_in_add` |  |
| `event:/infantry/player/weapon/antivehicle/_antivehicle_template/reload_shutter_in` |  |
| `event:/infantry/player/weapon/antivehicle/_antivehicle_template/reload_shutter_out` |  |
| `event:/infantry/player/weapon/antivehicle/_mc_antivehicle_template/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/_mc_antivehicle_template/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/_mc_antivehicle_template/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/atr_boys/bolt_action` |  |
| `event:/infantry/player/weapon/antivehicle/atr_boys/reload_mag_in` |  |
| `event:/infantry/player/weapon/antivehicle/atr_boys/reload_mag_out` |  |
| `event:/infantry/player/weapon/antivehicle/atr_boys/reload_shutter_in` |  |
| `event:/infantry/player/weapon/antivehicle/atr_boys/reload_shutter_out` |  |
| `event:/infantry/player/weapon/antivehicle/fim_92a_stinger/reload_foley_end` |  |
| `event:/infantry/player/weapon/antivehicle/fim_92a_stinger/reload_mag_in` |  |
| `event:/infantry/player/weapon/antivehicle/fim_92a_stinger/reload_mag_out` |  |
| `event:/infantry/player/weapon/antivehicle/fim_92a_stinger/reload_shutter_in` |  |
| `event:/infantry/player/weapon/antivehicle/gp_34/mod_reload` |  |
| `event:/infantry/player/weapon/antivehicle/grb_39/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/grb_39/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/grb_39/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/grb_39/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/igla/pzrk_target_active` |  |
| `event:/infantry/player/weapon/antivehicle/igla/pzrk_target_locked` |  |
| `event:/infantry/player/weapon/antivehicle/igla/pzrk_target_prepare` |  |
| `event:/infantry/player/weapon/antivehicle/javelin/reload_attach` |  |
| `event:/infantry/player/weapon/antivehicle/javelin/reload_mag_in` |  |
| `event:/infantry/player/weapon/antivehicle/javelin/reload_mag_out` |  |
| `event:/infantry/player/weapon/antivehicle/javelin/reload_prepare` |  |
| `event:/infantry/player/weapon/antivehicle/luftfaust_b/reload` |  |
| `event:/infantry/player/weapon/antivehicle/m136_at4/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/m136_at4/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/m136_at4/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/m136_at4/reload_foley_end` |  |
| `event:/infantry/player/weapon/antivehicle/m136_at4/reload_foley_start` |  |
| `event:/infantry/player/weapon/antivehicle/m1_bazooka/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/m1_bazooka/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/m1_bazooka/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/m203/mod_activate` |  |
| `event:/infantry/player/weapon/antivehicle/m203/mod_deactivate` |  |
| `event:/infantry/player/weapon/antivehicle/m203/mod_reload` |  |
| `event:/infantry/player/weapon/antivehicle/mortar_2b25/reload_shell_in` |  |
| `event:/infantry/player/weapon/antivehicle/mortar_rm_40/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/mortar_rm_40/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/mortar_rm_40/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/mortyr_grenade_launcher/mod_activate` |  |
| `event:/infantry/player/weapon/antivehicle/mortyr_grenade_launcher/mod_deactivate` |  |
| `event:/infantry/player/weapon/antivehicle/mortyr_grenade_launcher/mod_reload` |  |
| `event:/infantry/player/weapon/antivehicle/mpads_verba/reload_foley_end` |  |
| `event:/infantry/player/weapon/antivehicle/mpads_verba/reload_mag_in` |  |
| `event:/infantry/player/weapon/antivehicle/mpads_verba/reload_mag_out` |  |
| `event:/infantry/player/weapon/antivehicle/mpads_verba/reload_shutter_in` |  |
| `event:/infantry/player/weapon/antivehicle/neiman_minethrower/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/neiman_minethrower/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/neiman_minethrower/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/neiman_minethrower/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/panzerfaust_100/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/panzerfaust_100/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/panzerfaust_100/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/panzerschreck/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/panzerschreck/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/panzerschreck/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/piat/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/piat/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/piat/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/ptrs41/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/ptrs41/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/ptrs41/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/pzb39/bolt_action_1` |  |
| `event:/infantry/player/weapon/antivehicle/pzb39/bolt_action_2` |  |
| `event:/infantry/player/weapon/antivehicle/pzb39/bolt_action_3` |  |
| `event:/infantry/player/weapon/antivehicle/pzb39/bolt_action_4` |  |
| `event:/infantry/player/weapon/antivehicle/pzb39/bolt_action_5` |  |
| `event:/infantry/player/weapon/antivehicle/pzb39/bolt_action_6` |  |
| `event:/infantry/player/weapon/antivehicle/pzb39/bolt_action_7` |  |
| `event:/infantry/player/weapon/antivehicle/pzb39/bolt_action_8` |  |
| `event:/infantry/player/weapon/antivehicle/pzb39/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/pzb39/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/pzb39/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/pzb39/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/rpg_7/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/rpg_7/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/rpg_7/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/rpg_7/reload_foley_end` |  |
| `event:/infantry/player/weapon/antivehicle/rpg_7/reload_foley_start` |  |
| `event:/infantry/player/weapon/antivehicle/rpzb_43/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/rpzb_43/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/rpzb_43/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/antivehicle/type_5_rocket_launcher/reload_shell_in` |  |
| `event:/infantry/player/weapon/antivehicle/type_5_rocket_launcher/reload_shell_in_add` |  |
| `event:/infantry/player/weapon/antivehicle/type_5_rocket_launcher/reload_shutter_in` |  |
| `event:/infantry/player/weapon/antivehicle/type_5_rocket_launcher/reload_shutter_out` |  |
| `event:/infantry/player/weapon/antivehicle/type_97_antitank/reload` |  |
| `event:/infantry/player/weapon/antivehicle/type_97_antitank/reload_alt` |  |
| `event:/infantry/player/weapon/antivehicle/vpgs_grenade_launcher/mod_activate` |  |
| `event:/infantry/player/weapon/antivehicle/vpgs_grenade_launcher/mod_deactivate` |  |
| `event:/infantry/player/weapon/antivehicle/vpgs_grenade_launcher/mod_reload` |  |
| `event:/infantry/player/weapon/antivehicle/wz_35/bolt_action` |  |
| `event:/infantry/player/weapon/antivehicle/wz_35/reload_mag_in` |  |
| `event:/infantry/player/weapon/antivehicle/wz_35/reload_mag_out` |  |
| `event:/infantry/player/weapon/antivehicle/wz_35/reload_shutter_in` |  |
| `event:/infantry/player/weapon/antivehicle/wz_35/reload_shutter_out` |  |
| `event:/infantry/player/weapon/explosive/activate` |  |
| `event:/infantry/player/weapon/explosive/drop` | Distance |
| `event:/infantry/player/weapon/explosive/throw` |  |
| `event:/infantry/player/weapon/grenade/activate` |  |
| `event:/infantry/player/weapon/grenade/activate_with_clap` |  |
| `event:/infantry/player/weapon/grenade/drop` | Distance |
| `event:/infantry/player/weapon/grenade/throw` |  |
| `event:/infantry/player/weapon/grenade_flash/activate` |  |
| `event:/infantry/player/weapon/grenade_flash/drop` | Distance |
| `event:/infantry/player/weapon/grenade_flash/throw` |  |
| `event:/infantry/player/weapon/incendiary_grenade/activate` |  |
| `event:/infantry/player/weapon/melee/aspen_stake/whoosh` |  |
| `event:/infantry/player/weapon/melee/axe/whoosh` |  |
| `event:/infantry/player/weapon/melee/bat/whoosh` |  |
| `event:/infantry/player/weapon/melee/hands/whoosh` |  |
| `event:/infantry/player/weapon/melee/knife/whoosh` |  |
| `event:/infantry/player/weapon/melee/lunge_mine/whoosh` |  |
| `event:/infantry/player/weapon/melee/machete/whoosh` |  |
| `event:/infantry/player/weapon/melee/mgun/whoosh` |  |
| `event:/infantry/player/weapon/melee/pipe/whoosh` |  |
| `event:/infantry/player/weapon/melee/pistol/whoosh` |  |
| `event:/infantry/player/weapon/melee/rifle/whoosh` |  |
| `event:/infantry/player/weapon/melee/shovel/whoosh` |  |
| `event:/infantry/player/weapon/melee/sword/whoosh` |  |
| `event:/infantry/player/weapon/mgun/ab_46/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ab_46/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ab_46/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ab_46/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ab_46/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_103/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_103/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_103/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_12/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/ak_12/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/ak_12/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/ak_12/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/ak_12/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/ak_12/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/ak_47/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_47/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_47/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_47/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_47/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_74/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_74/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_74/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_74/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ak_74/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/akm/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/akm/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/akm/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/akm/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/akm/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/an_94/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/an_94/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/an_94/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/an_94/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/an_94/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/an_m2_stinger/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/an_m2_stinger/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/an_m2_stinger/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/an_m2_stinger/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/an_m2_stinger/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/an_m2_stinger/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/an_m2_stinger/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/an_m2_stinger/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/an_m2_stinger/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/an_m2_stinger/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/as_44/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/as_44/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/as_44/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/as_val/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/as_val/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/as_val/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/as_val/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/as_val/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/as_val/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/at_44/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/at_44/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/at_44/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/at_44/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/avs36/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/avs36/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/avs36/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/beretta_m1918/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/beretta_m1918/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/beretta_m1918/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/besal_lmg/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/besal_lmg/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/besal_lmg/reload6/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/besal_lmg/reload7/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/breda_mod_30/reload` |  |
| `event:/infantry/player/weapon/mgun/breda_mod_30/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/bren_100_round_drum/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/bren_100_round_drum/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/bren_100_round_drum/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/bren_100_round_drum/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/bren_100_round_drum/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/bren_100_round_drum/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/bren_100_round_drum/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/bren_100_round_drum/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/charlton/reload` |  |
| `event:/infantry/player/weapon/mgun/charlton/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/chatellerault_m_24_29/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/chatellerault_m_24_29/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/chatellerault_m_24_29/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/chatellerault_m_24_29/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/chatellerault_m_24_29/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/chauchat/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/chauchat/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/chauchat/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/chauchat/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/chauchat/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/coenders_mp/reload` |  |
| `event:/infantry/player/weapon/mgun/coenders_mp/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/coenders_smg/reload` |  |
| `event:/infantry/player/weapon/mgun/coenders_smg/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/colt_9_mm_smg/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/colt_9_mm_smg/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/colt_9_mm_smg/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/colt_9_mm_smg/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/colt_9_mm_smg/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/cz_bren_2/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/cz_bren_2/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/cz_bren_2/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/danuvia_43m/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/danuvia_43m/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/danuvia_43m/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/dp27/reload` |  |
| `event:/infantry/player/weapon/mgun/dp27/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/dp27/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/dp27/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/dp27/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/dp27/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/dp27/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/dp_42_beltfed/reload` |  |
| `event:/infantry/player/weapon/mgun/dp_42_beltfed/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/dpm/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/dpm/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/dpm/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/dpm/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/dpm/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/erma_emp/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/erma_emp/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/erma_emp/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fedorov/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fedorov/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fedorov/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fg42/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fg42/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fg42/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fg42_m2/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fg42_m2/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fg42_m2/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fn_m1930/reload` |  |
| `event:/infantry/player/weapon/mgun/fn_m1930/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/fn_scar_h/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fn_scar_h/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fn_scar_h/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fnab_43/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fnab_43/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/fnab_43/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/gorov_mg/reload` |  |
| `event:/infantry/player/weapon/mgun/gorov_mg/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/hk_mp5/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/hk_mp5/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/hk_mp5/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/hk_mp5/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/hk_mp7a2/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/hk_mp7a2/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/hk_mp7a2/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/hk_mp7a2/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/hk_mp7a2/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/hk_mp7a2/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/horn_sturmgewehr/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/horn_sturmgewehr/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/horn_sturmgewehr/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/hotchkiss_m1922/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/hotchkiss_m1922/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/hotchkiss_m1922/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/hotchkiss_m1922/reload_mag_in_add` |  |
| `event:/infantry/player/weapon/mgun/hotchkiss_m1922/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/hotchkiss_m1922/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/hotchkiss_m1922/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/hotchkiss_m1922/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/hotchkiss_m1922/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/hyde_model_35/reload` |  |
| `event:/infantry/player/weapon/mgun/hyde_model_35/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/hyde_model_35/reload_dual` |  |
| `event:/infantry/player/weapon/mgun/knorr_bremse_mg_35_36/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/knorr_bremse_mg_35_36/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/knorr_bremse_mg_35_36/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/knorr_bremse_mg_35_36/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/knorr_bremse_mg_35_36/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/knorr_bremse_mg_35_36/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/krieghoff_fg/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/krieghoff_fg/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/krieghoff_fg/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/kriss_vector/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/kriss_vector/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/kriss_vector/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/kriss_vector/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/kriss_vector/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/kriss_vector/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/kriss_vector/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/lad/reload` |  |
| `event:/infantry/player/weapon/mgun/lad/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/lahti_saloranta_m26/reload` |  |
| `event:/infantry/player/weapon/mgun/lahti_saloranta_m26/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/lahti_saloranta_m26/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/lahti_saloranta_m26/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/lahti_saloranta_m26/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/lahti_saloranta_m26/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/lahti_saloranta_m26/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/lanchester_model_1/reload` |  |
| `event:/infantry/player/weapon/mgun/lanchester_model_1/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/lewis/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/lewis/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/lewis/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/lewis/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/lewis/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m1/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m1/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m1/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m16a4/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/m16a4/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/m16a4/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/m16a4/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/m16a4/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/m1918/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m1918/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m1918/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m1918/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m1919a6/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/m1919a6/reload_belt_out` |  |
| `event:/infantry/player/weapon/mgun/m1919a6/reload_belt_rattle` |  |
| `event:/infantry/player/weapon/mgun/m1919a6/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/m1919a6/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/m1919a6/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/m1919a6/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/m1919a6/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/m1919a6/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/m1919a6/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/m1919a6/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/m240/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/m240/reload_belt_out` |  |
| `event:/infantry/player/weapon/mgun/m240/reload_belt_rattle` |  |
| `event:/infantry/player/weapon/mgun/m240/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/m240/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/m240/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/m240/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/m240/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/m240/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/m240/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/m240/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/m249/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/m249/reload_belt_out` |  |
| `event:/infantry/player/weapon/mgun/m249/reload_belt_rattle` |  |
| `event:/infantry/player/weapon/mgun/m249/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/m249/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/m249/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/m249/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/m249/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/m249/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/m249/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/m249/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/m27_iar/reload_bolt_punch` |  |
| `event:/infantry/player/weapon/mgun/m27_iar/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/m27_iar/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/m27_iar/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/m27_iar/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/m27_iar/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/m3/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m3/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m3/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m3/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m38/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m38/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m38/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m4/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m4/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m4/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m4a1/reload_drum_in` |  |
| `event:/infantry/player/weapon/mgun/m4a1/reload_drum_out` |  |
| `event:/infantry/player/weapon/mgun/m4a1/reload_drum_punch` |  |
| `event:/infantry/player/weapon/mgun/m4a1/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/m4a1/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/m4a1/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/m4a1/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/m4a1/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/m50/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m50/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m50/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/m50/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mac_11/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mac_11/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mac_11/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mac_11/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mac_11/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/mac_11/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/mac_11/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/mac_11/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/mac_11/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/madsen/reload` |  |
| `event:/infantry/player/weapon/mgun/madsen/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/maxim_tokarev/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/maxim_tokarev/reload_belt_out` |  |
| `event:/infantry/player/weapon/mgun/maxim_tokarev/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/maxim_tokarev/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/maxim_tokarev/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/maxim_tokarev/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/maxim_tokarev/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/mg42/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg42/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg42/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg42/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg42/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg42/reload6/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg42/reload7/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg42/reload8/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_13/reload` |  |
| `event:/infantry/player/weapon/mgun/mg_13/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_13/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_13/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_13/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_13/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_13/reload6/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_13/reload7/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_13/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/mg_15/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/mg_15/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/mg_15/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/mg_15/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/mg_15/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/mg_15/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/mg_15/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/mg_30/reload` |  |
| `event:/infantry/player/weapon/mgun/mg_30/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/mg_34/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_34/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_34/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_34/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_34/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_34/reload6/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_34/reload7/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mg_34_patronentrommel/reload` |  |
| `event:/infantry/player/weapon/mgun/mg_34_patronentrommel/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/mg_42_beltfed/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/mg_42_beltfed/reload_belt_out` |  |
| `event:/infantry/player/weapon/mgun/mg_42_beltfed/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/mg_42_beltfed/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/mg_42_beltfed/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/mg_42_beltfed/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/mg_42_beltfed/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/mg_42_beltfed/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/mg_81_infantry/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/mg_81_infantry/reload_belt_out` |  |
| `event:/infantry/player/weapon/mgun/mg_81_infantry/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/mg_81_infantry/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/mg_81_infantry/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/mg_81_infantry/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/mg_81_infantry/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/mk_48/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/mk_48/reload_belt_out` |  |
| `event:/infantry/player/weapon/mgun/mk_48/reload_belt_rattle` |  |
| `event:/infantry/player/weapon/mgun/mk_48/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/mk_48/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/mk_48/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/mk_48/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/mk_48/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/mk_48/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/mk_48/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/mk_48/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/mkb_42_w/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mkb_42_w/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mkb_42_w/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp18/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp18/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp18/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp34o/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp34o/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp34o/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp35/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp35/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp35/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp40/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp40/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp40/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/mp40/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/nambu_type_1_early_smg/reload` |  |
| `event:/infantry/player/weapon/mgun/nambu_type_1_early_smg/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/nambu_type_1_smg/reload` |  |
| `event:/infantry/player/weapon/mgun/nambu_type_1_smg/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/nambu_type_2a_smg/reload` |  |
| `event:/infantry/player/weapon/mgun/nambu_type_2a_smg/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/nambu_type_99_lmg/reload` |  |
| `event:/infantry/player/weapon/mgun/nambu_type_99_lmg/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/pkp_pecheneg/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/pkp_pecheneg/reload_belt_rattle` |  |
| `event:/infantry/player/weapon/mgun/pkp_pecheneg/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/pkp_pecheneg/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/pkp_pecheneg/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/pkp_pecheneg/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/pkp_pecheneg/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/pkp_pecheneg/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/pkp_pecheneg/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/pkp_pecheneg/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/pp_19_bizon/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/pp_19_bizon/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/pp_19_bizon/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/pp_19_bizon/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/pp_19_bizon/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/pp_19_bizon/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/pp_19_bizon/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/pp_19_bizon/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/pp_19_vityaz/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/pp_19_vityaz/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/pp_19_vityaz/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/pp_19_vityaz/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/pp_19_vityaz/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/pp_19_vityaz/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/pp_2000/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/pp_2000/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/pp_2000/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/pp_2000/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/pp_2000/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/pp_2000/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/pp_2000/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/pp_2000/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/pp_71/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/pp_71/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/pp_71/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/pp_71/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/pp_71/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/pp_71/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/pp_71/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/pp_71/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/pp_dolganov/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/pp_dolganov/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/pp_dolganov/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/pp_dolganov/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppd3438/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppd3438/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppd3438/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppd3438_box/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppd3438_box/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppd3438_box/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppd40/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppd40/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppd40/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppk_41/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppk_41/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppk_41/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/pps_42/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/pps_42/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/pps_42/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppsh/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppsh/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppsh/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppsh/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/ppsh_40/reload` |  |
| `event:/infantry/player/weapon/mgun/ppsh_40/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload6/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload7/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload_belt_rattle` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/rd_44/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/rp_46/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/rp_46/reload_belt_out` |  |
| `event:/infantry/player/weapon/mgun/rp_46/reload_belt_rattle` |  |
| `event:/infantry/player/weapon/mgun/rp_46/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/rp_46/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/rp_46/reload_mag_latch_lock` |  |
| `event:/infantry/player/weapon/mgun/rp_46/reload_mag_latch_unlock` |  |
| `event:/infantry/player/weapon/mgun/rp_46/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/rp_46/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/rp_46/reload_shutter` |  |
| `event:/infantry/player/weapon/mgun/rpk_16/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rpk_16/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rpk_16/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rpk_16/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rpk_16/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rpk_1943/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/rpk_1943/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/rpk_1943/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/rpk_1943/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/rpk_1943/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/rpk_1943/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/rpk_74m/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rpk_74m/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rpk_74m/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rpk_74m/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/rpk_74m/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/schmeisser_mk36/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/schmeisser_mk36/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/schmeisser_mk36/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/scorpion_evo_3/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/scorpion_evo_3/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/scorpion_evo_3/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/scorpion_evo_3/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/scorpion_evo_3/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/scorpion_evo_3/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/scorpion_evo_3/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/sig_1920/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/sig_1920/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/sig_1920/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/sig_ke_7/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/sig_ke_7/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/sig_ke_7/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/sig_ke_7/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/sig_xm250/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/sig_xm250/reload_belt_out` |  |
| `event:/infantry/player/weapon/mgun/sig_xm250/reload_belt_rattle` |  |
| `event:/infantry/player/weapon/mgun/sig_xm250/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/sig_xm250/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/sig_xm250/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/sig_xm250/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/sig_xm250/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/sig_xm250/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/sig_xm250/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/sig_xm250/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/sig_xm5/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/sig_xm5/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/sig_xm5/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/sig_xm5/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/sig_xm5/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/sig_xm5/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/sig_xm5/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/sten_mk2/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/sten_mk2/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/sten_mk2/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/steyr_aug/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/steyr_aug/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/steyr_aug/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/stg_44/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/stg_44/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/stg_44/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/stg_44/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/suomi_kp_31/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/suomi_kp_31/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/suomi_kp_31/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/t24_mg/reload_belt_in` |  |
| `event:/infantry/player/weapon/mgun/t24_mg/reload_belt_out` |  |
| `event:/infantry/player/weapon/mgun/t24_mg/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/t24_mg/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/t24_mg/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/t24_mg/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/t24_mg/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/t24_mg/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/thompson/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/thompson/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/thompson/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/thompson/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/thompson_100_drum/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/thompson_100_drum/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/thompson_100_drum/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/thompson_100_drum/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/thompson_m1921ac/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/thompson_m1921ac/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/thompson_m1921ac/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/thompson_m1921ac/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/thompson_m1921ac/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/thompson_m1921ac/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/thompson_m1928a1_50_drum/reload` |  |
| `event:/infantry/player/weapon/mgun/thompson_m1928a1_50_drum/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/tokyo_arsenal_model_1927/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/tokyo_arsenal_model_1927/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/tokyo_arsenal_model_1927/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/tokyo_arsenal_model_1927/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/type_100_mg/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/type_100_mg/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/type_100_mg/reload_mag_punch` |  |
| `event:/infantry/player/weapon/mgun/type_100_mg/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/type_100_mg/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/type_100_mg/reload_shutter_out` |  |
| `event:/infantry/player/weapon/mgun/type_100_smg/reload` |  |
| `event:/infantry/player/weapon/mgun/type_100_smg/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/ud_m42/reload` |  |
| `event:/infantry/player/weapon/mgun/ud_m42/reload_alt` |  |
| `event:/infantry/player/weapon/mgun/vollmer_m35/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/vollmer_m35/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/vollmer_m35/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/yazikov_smg/reload_foley_end` |  |
| `event:/infantry/player/weapon/mgun/yazikov_smg/reload_foley_start` |  |
| `event:/infantry/player/weapon/mgun/yazikov_smg/reload_mag_in` |  |
| `event:/infantry/player/weapon/mgun/yazikov_smg/reload_mag_out` |  |
| `event:/infantry/player/weapon/mgun/yazikov_smg/reload_shutter_in` |  |
| `event:/infantry/player/weapon/mgun/zb_26/reload` |  |
| `event:/infantry/player/weapon/mgun/zb_26/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/zb_26/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/zb_26/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/zb_26/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/zb_26/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/zb_26/reload6/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/zb_26/reload7/change_ammo` |  |
| `event:/infantry/player/weapon/mgun/zb_26/reload_alt` |  |
| `event:/infantry/player/weapon/mine/activate` |  |
| `event:/infantry/player/weapon/mine/throw` |  |
| `event:/infantry/player/weapon/misc/flamethrower/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/misc/flamethrower/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/misc/flamethrower/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/molotov/activate` |  |
| `event:/infantry/player/weapon/molotov/throw` |  |
| `event:/infantry/player/weapon/pistol/_pistol_template/mag_in` |  |
| `event:/infantry/player/weapon/pistol/_pistol_template/mag_out` |  |
| `event:/infantry/player/weapon/pistol/_pistol_template/shutter_in` |  |
| `event:/infantry/player/weapon/pistol/_pistol_template/shutter_out` |  |
| `event:/infantry/player/weapon/pistol/beretta_m1923/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/beretta_m9/reload_foley_end` |  |
| `event:/infantry/player/weapon/pistol/beretta_m9/reload_foley_start` |  |
| `event:/infantry/player/weapon/pistol/beretta_m9/reload_mag_in` |  |
| `event:/infantry/player/weapon/pistol/beretta_m9/reload_mag_out` |  |
| `event:/infantry/player/weapon/pistol/beretta_m9/reload_mag_punch` |  |
| `event:/infantry/player/weapon/pistol/beretta_m9/reload_shutter_out` |  |
| `event:/infantry/player/weapon/pistol/c96/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/c96/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/c96/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/c96_m712/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/c96_m712/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/c96_m712/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/colt_new_service/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/colt_new_service/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/colt_new_service/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/dreyse_m1907/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/dreyse_m1907/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/dreyse_m1907/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/m1911/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/m1911/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/m1911/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/m45a1_cqbp/reload_foley_end` |  |
| `event:/infantry/player/weapon/pistol/m45a1_cqbp/reload_foley_start` |  |
| `event:/infantry/player/weapon/pistol/m45a1_cqbp/reload_mag_in` |  |
| `event:/infantry/player/weapon/pistol/m45a1_cqbp/reload_mag_out` |  |
| `event:/infantry/player/weapon/pistol/m45a1_cqbp/reload_mag_punch` |  |
| `event:/infantry/player/weapon/pistol/m45a1_cqbp/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/pistol/m45a1_cqbp/reload_shutter_out` |  |
| `event:/infantry/player/weapon/pistol/makarov/reload_foley_end` |  |
| `event:/infantry/player/weapon/pistol/makarov/reload_foley_start` |  |
| `event:/infantry/player/weapon/pistol/makarov/reload_mag_in` |  |
| `event:/infantry/player/weapon/pistol/makarov/reload_mag_out` |  |
| `event:/infantry/player/weapon/pistol/makarov/reload_mag_punch` |  |
| `event:/infantry/player/weapon/pistol/makarov/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/pistol/makarov/reload_shutter_out` |  |
| `event:/infantry/player/weapon/pistol/mp_443/reload_foley_end` |  |
| `event:/infantry/player/weapon/pistol/mp_443/reload_foley_start` |  |
| `event:/infantry/player/weapon/pistol/mp_443/reload_mag_in` |  |
| `event:/infantry/player/weapon/pistol/mp_443/reload_mag_out` |  |
| `event:/infantry/player/weapon/pistol/mp_443/reload_mag_punch` |  |
| `event:/infantry/player/weapon/pistol/mp_443/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/pistol/mp_443/reload_shutter_in` |  |
| `event:/infantry/player/weapon/pistol/mp_443/reload_shutter_out` |  |
| `event:/infantry/player/weapon/pistol/nagant_1895/bolt_action` |  |
| `event:/infantry/player/weapon/pistol/nagant_1895/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/nagant_1895/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/nagant_1895/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/p08/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/p08/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/p08/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/p08/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/p38/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/p38/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/p38/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/sturmpistole/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/sturmpistole/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/sturmpistole/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/sturmpistole/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/sturmpistole/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/sturmpistole/reload6/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/sturmpistole/reload7/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/sw_m1917/bolt_action` |  |
| `event:/infantry/player/weapon/pistol/tk_26/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/tk_26/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/tk_26/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/tt/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/tt/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/tt/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/voevodin_pistol/reload` |  |
| `event:/infantry/player/weapon/pistol/voevodin_pistol/reload_alt` |  |
| `event:/infantry/player/weapon/pistol/walther_pp/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/walther_pp/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/walther_pp/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/pistol/welrod_mk2/reload_mag_in` |  |
| `event:/infantry/player/weapon/pistol/welrod_mk2/reload_mag_out` |  |
| `event:/infantry/player/weapon/pistol/welrod_mk2/reload_shutter_in` |  |
| `event:/infantry/player/weapon/pistol/welrod_mk2/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/_rifle_template/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/_rifle_template/mod_activate` |  |
| `event:/infantry/player/weapon/rifle/_rifle_template/mod_deactivate` |  |
| `event:/infantry/player/weapon/rifle/_rifle_template/mod_reload` |  |
| `event:/infantry/player/weapon/rifle/_rifle_template/reload_loop` |  |
| `event:/infantry/player/weapon/rifle/_rifle_template/reload_post` |  |
| `event:/infantry/player/weapon/rifle/_rifle_template/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_38/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_38/reload` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_38/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_38/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_38/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_38/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_38/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_early_short/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_early_short/reload` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_early_short/reload_loop` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_early_short/reload_post` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_early_short/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_early_sniper/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_early_sniper/reload` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_early_sniper/reload_loop` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_early_sniper/reload_post` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_early_sniper/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_late/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_late/reload` | mat |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_late/reload_loop` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_late/reload_post` |  |
| `event:/infantry/player/weapon/rifle/arisaka_type_99_late/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/armaguerra_mod_39/ammo_eject` |  |
| `event:/infantry/player/weapon/rifle/armaguerra_mod_39/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/armaguerra_mod_39/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/armaguerra_mod_39/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/armaguerra_mod_39/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/armaguerra_mod_39/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/avt_40/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/avt_40/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/avt_40/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/barrett_m82a1/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/barrett_m82a1/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/barrett_m82a1/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/barrett_m82a1/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/barrett_m82a1/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/barrett_m82a1/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/barrett_m82a1/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/barrett_m82a1/reload_mag_punch` |  |
| `event:/infantry/player/weapon/rifle/barrett_m82a1/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/barrett_m82a1/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/beretta_m31/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/beretta_m31/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/beretta_m31/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/beretta_m31/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/beretta_m31/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/berthier_m16/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/berthier_m16/reload` |  |
| `event:/infantry/player/weapon/rifle/berthier_m16/reload_alt` |  |
| `event:/infantry/player/weapon/rifle/breda_m1935_pg/reload` |  |
| `event:/infantry/player/weapon/rifle/breda_m1935_pg/reload_alt` |  |
| `event:/infantry/player/weapon/rifle/browning_auto_5/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/browning_auto_5/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/browning_auto_5/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/carcano_m41/ammo_eject` |  |
| `event:/infantry/player/weapon/rifle/carcano_m41/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/carcano_m41/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/carcano_m41/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/carcano_m41/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/carcano_m41/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/delisle_commando_carbine/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/delisle_commando_carbine/reload3` |  |
| `event:/infantry/player/weapon/rifle/delisle_commando_carbine/reload4` |  |
| `event:/infantry/player/weapon/rifle/dp_12/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/dp_12/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/dp_12/reload_shell_in` |  |
| `event:/infantry/player/weapon/rifle/dp_12/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/dp_12/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/farquhar_hill_1918/reload` |  |
| `event:/infantry/player/weapon/rifle/farquhar_hill_1918/reload_alt` |  |
| `event:/infantry/player/weapon/rifle/fedorov_rifle_5_rounds/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/fedorov_rifle_5_rounds/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/fedorov_rifle_5_rounds/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/fedorov_rifle_5_rounds/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/fedorov_rifle_5_rounds/reload_shell_in` |  |
| `event:/infantry/player/weapon/rifle/fedorov_rifle_5_rounds/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/fedorov_rifle_5_rounds/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/gewehr41/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/gewehr41/reload` |  |
| `event:/infantry/player/weapon/rifle/gewehr41/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/gewehr41/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/gewehr41/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/gewehr41/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/gewehr41/reload_loop_multiple` |  |
| `event:/infantry/player/weapon/rifle/gewehr41/reload_loop_single` |  |
| `event:/infantry/player/weapon/rifle/gewehr41/reload_post` |  |
| `event:/infantry/player/weapon/rifle/gewehr41/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/gewehr43/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/gewehr43/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/gewehr43/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/gewehr43/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/gewehr43/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/gewehr_88/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/hino_komuro_m1904/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/hino_komuro_m1904/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/hino_komuro_m1904/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/hino_komuro_m1904/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/hino_komuro_m1904/reload_mag_punch` |  |
| `event:/infantry/player/weapon/rifle/hino_komuro_m1904/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/hk_g3a4/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/hk_g3a4/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/hk_g3a4/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/hk_g3a4/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/hk_g3a4/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/hk_g3a4/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/ithaca_37/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/ithaca_37/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/ithaca_37/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/ithaca_37/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/kar98k_kriegsmodell/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/kar98k_kriegsmodell/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/kar98k_kriegsmodell/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/kar98k_kriegsmodell/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/kar98k_kriegsmodell/reload6/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/koko_rifle/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/koko_rifle/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/koko_rifle/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/koko_rifle/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/koko_rifle/reload_shell_in` |  |
| `event:/infantry/player/weapon/rifle/koko_rifle/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/koko_rifle/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/ks_p_18_5/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/ks_p_18_5/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/ks_p_18_5/reload_shell_in` |  |
| `event:/infantry/player/weapon/rifle/ks_p_18_5/reload_shell_second_in` |  |
| `event:/infantry/player/weapon/rifle/ksvk_12_7/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/ksvk_12_7/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/ksvk_12_7/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/ksvk_12_7/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/lebel_1886_m93/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/lebel_1886_m93/reload_loop` |  |
| `event:/infantry/player/weapon/rifle/lebel_1886_m93/reload_post` |  |
| `event:/infantry/player/weapon/rifle/lebel_1886_m93/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/lee_enfield/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/lee_enfield/reload` |  |
| `event:/infantry/player/weapon/rifle/lee_enfield/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/lee_enfield/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/lee_enfield/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/lee_enfield/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/lee_enfield/reload_loop_multiple` |  |
| `event:/infantry/player/weapon/rifle/lee_enfield/reload_loop_single` |  |
| `event:/infantry/player/weapon/rifle/lee_enfield/reload_post` |  |
| `event:/infantry/player/weapon/rifle/lee_enfield/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/liu_rifle/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/liu_rifle/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/liu_rifle/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/liu_rifle/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/liu_rifle/reload_shell_in` |  |
| `event:/infantry/player/weapon/rifle/liu_rifle/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/liu_rifle/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/lw_3/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/lw_3/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/lw_3/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1/ammo_eject` |  |
| `event:/infantry/player/weapon/rifle/m1/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/m1/mod_activate` |  |
| `event:/infantry/player/weapon/rifle/m1/mod_deactivate` |  |
| `event:/infantry/player/weapon/rifle/m1/mod_reload` |  |
| `event:/infantry/player/weapon/rifle/m1/reload` |  |
| `event:/infantry/player/weapon/rifle/m1/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1/reload_alt` |  |
| `event:/infantry/player/weapon/rifle/m110a1_sdmr/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/m110a1_sdmr/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/m110a1_sdmr/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/m110a1_sdmr/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/m110a1_sdmr/reload_mag_punch` |  |
| `event:/infantry/player/weapon/rifle/m110a1_sdmr/reload_mag_punch_2` |  |
| `event:/infantry/player/weapon/rifle/m1903/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/m1903/reload` |  |
| `event:/infantry/player/weapon/rifle/m1903/reload_loop` |  |
| `event:/infantry/player/weapon/rifle/m1903/reload_post` |  |
| `event:/infantry/player/weapon/rifle/m1903/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/m1903_pedersen/reload` |  |
| `event:/infantry/player/weapon/rifle/m1903_pedersen/reload_alt` |  |
| `event:/infantry/player/weapon/rifle/m1903_springfield/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/m1903_springfield/reload` |  |
| `event:/infantry/player/weapon/rifle/m1903_springfield/reload_loop_multiple` |  |
| `event:/infantry/player/weapon/rifle/m1903_springfield/reload_loop_single` |  |
| `event:/infantry/player/weapon/rifle/m1903_springfield/reload_post` |  |
| `event:/infantry/player/weapon/rifle/m1903_springfield/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/m1917_enfield/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/m1917_enfield/reload` |  |
| `event:/infantry/player/weapon/rifle/m1917_enfield/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1917_enfield/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1917_enfield/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1917_enfield/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1917_enfield/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1941_johnson/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/m1941_johnson/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1941_johnson/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1941_johnson/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1941_johnson/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1941_johnson/reload_loop_multiple` |  |
| `event:/infantry/player/weapon/rifle/m1941_johnson/reload_loop_single` |  |
| `event:/infantry/player/weapon/rifle/m1941_johnson/reload_post` |  |
| `event:/infantry/player/weapon/rifle/m1941_johnson/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/m1a1_carbine/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1a1_carbine/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m1a1_carbine/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m24/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/m24/reload` |  |
| `event:/infantry/player/weapon/rifle/m24/reload_loop` |  |
| `event:/infantry/player/weapon/rifle/m24/reload_post` |  |
| `event:/infantry/player/weapon/rifle/m24/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/m30_luftwaffe/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m30_luftwaffe/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m30_luftwaffe/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m30_luftwaffe/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/m30_luftwaffe/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mannlicher_m1895/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/mannlicher_m1895/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mannlicher_m1895/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mannlicher_m1895/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mannlicher_m1895/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mannlicher_m93_roman/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/mannlicher_m93_roman/reload` |  |
| `event:/infantry/player/weapon/rifle/mannlicher_m93_roman/reload_alt` |  |
| `event:/infantry/player/weapon/rifle/mas_36/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/mas_36/reload` |  |
| `event:/infantry/player/weapon/rifle/mas_36/reload_loop` |  |
| `event:/infantry/player/weapon/rifle/mas_36/reload_post` |  |
| `event:/infantry/player/weapon/rifle/mas_36/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/mauser98k/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/mauser98k/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mauser98k/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mauser98k/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mauser98k/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mauser98k/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mauser98k/reload6/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mauser98k/reload7/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mauser98k/reload_loop_multiple` |  |
| `event:/infantry/player/weapon/rifle/mauser98k/reload_loop_single` |  |
| `event:/infantry/player/weapon/rifle/mauser98k/reload_post` |  |
| `event:/infantry/player/weapon/rifle/mauser98k/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/mauser_gewehr_98_warmod/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/mauser_gewehr_98_warmod/reload_loop_multiple` |  |
| `event:/infantry/player/weapon/rifle/mauser_gewehr_98_warmod/reload_loop_single` |  |
| `event:/infantry/player/weapon/rifle/mauser_gewehr_98_warmod/reload_post` |  |
| `event:/infantry/player/weapon/rifle/mauser_gewehr_98_warmod/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/mcmillan_tac_50/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/mcmillan_tac_50/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/mcmillan_tac_50/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/mcmillan_tac_50/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/mcmillan_tac_50/reload_mag_punch` |  |
| `event:/infantry/player/weapon/rifle/mcmillan_tac_50/reload_shell_out` | mat |
| `event:/infantry/player/weapon/rifle/mcmillan_tac_50/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/mcmillan_tac_50/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/meunier_a6_carbine/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/meunier_a6_carbine/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/meunier_a6_carbine/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/meunier_a6_carbine/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/meunier_a6_carbine/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/meunier_a6_carbine/reload_shell_in` |  |
| `event:/infantry/player/weapon/rifle/meunier_a6_carbine/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/meunier_a6_carbine/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/mk_14_ebr/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/mk_14_ebr/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/mk_14_ebr/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/mk_14_ebr/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/mk_14_ebr/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/mondragon/reload` |  |
| `event:/infantry/player/weapon/rifle/mondragon/reload_alt` |  |
| `event:/infantry/player/weapon/rifle/mosin/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/mosin/reload` |  |
| `event:/infantry/player/weapon/rifle/mosin/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mosin/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mosin/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mosin/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mosin/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/mosin/reload_clip_out` |  |
| `event:/infantry/player/weapon/rifle/mosin/reload_loop` |  |
| `event:/infantry/player/weapon/rifle/mosin/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/mosin/reload_post` |  |
| `event:/infantry/player/weapon/rifle/mosin/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/mosin_1928/reload` |  |
| `event:/infantry/player/weapon/rifle/mosin_m1907/reload` |  |
| `event:/infantry/player/weapon/rifle/mossberg_590/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/mossberg_590/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/mossberg_590/reload_shell_in` |  |
| `event:/infantry/player/weapon/rifle/mossberg_590/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/mossberg_590/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/pavesi_m42/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/pavesi_m42/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/pavesi_m42/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/pavesi_m42/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/pavesi_m42/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/pavesi_prototype_svt_copy/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/pavesi_prototype_svt_copy/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/pavesi_prototype_svt_copy/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/pavesi_prototype_svt_copy/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/pavesi_prototype_svt_copy/reload_shell_in` |  |
| `event:/infantry/player/weapon/rifle/pavesi_prototype_svt_copy/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/pavesi_prototype_svt_copy/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/remington_870/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/remington_870/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/remington_870/reload_shell_in` |  |
| `event:/infantry/player/weapon/rifle/remington_870/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/remington_870/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/ross_rifle/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/ross_rifle/reload` |  |
| `event:/infantry/player/weapon/rifle/ross_rifle/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/ross_rifle/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/ross_rifle/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/ross_rifle/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/ross_rifle/reload_loop` |  |
| `event:/infantry/player/weapon/rifle/ross_rifle/reload_post` |  |
| `event:/infantry/player/weapon/rifle/ross_rifle/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/sks_30/reload_clip_out` |  |
| `event:/infantry/player/weapon/rifle/sks_30/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/sks_30/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/sks_30/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/sks_30/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/sks_30/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/sks_30/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/sks_30/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/sks_30/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/sks_31/reload` |  |
| `event:/infantry/player/weapon/rifle/sks_31/reload_loop` |  |
| `event:/infantry/player/weapon/rifle/sks_31/reload_post` |  |
| `event:/infantry/player/weapon/rifle/sks_31/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/spas_12/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/spas_12/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/spas_12/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/spas_12/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/stl_mosin_m91_30/reload` |  |
| `event:/infantry/player/weapon/rifle/sv_98/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/sv_98/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/sv_98/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/sv_98/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/sv_98/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/sv_98/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/svch/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/svch/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/svch/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/svch/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/svch/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/svd_m/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/svd_m/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/svd_m/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/svd_m/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/svd_m/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/svt40/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/svt40/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/svt40/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/svt40/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/svt40/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/svt40/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/svt40/reload6/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/sw_light_rifle/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/t20_early_rifle/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/t20_early_rifle/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/t20_early_rifle/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/t20_early_rifle/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/t20_rifle/reload` |  |
| `event:/infantry/player/weapon/rifle/t20_rifle/reload_alt` |  |
| `event:/infantry/player/weapon/rifle/turner/reload_loop_multiple` |  |
| `event:/infantry/player/weapon/rifle/turner/reload_loop_single` |  |
| `event:/infantry/player/weapon/rifle/turner/reload_post` |  |
| `event:/infantry/player/weapon/rifle/turner/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/type_22_murata/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/type_22_murata/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/type_22_murata/reload_mag_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/type_22_murata/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/type_22_murata/reload_shell_in` |  |
| `event:/infantry/player/weapon/rifle/type_22_murata/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/type_22_murata/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/type_4/reload_loop_multiple` |  |
| `event:/infantry/player/weapon/rifle/type_4/reload_loop_single` |  |
| `event:/infantry/player/weapon/rifle/type_4/reload_post` |  |
| `event:/infantry/player/weapon/rifle/type_4/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/type_hei/reload` |  |
| `event:/infantry/player/weapon/rifle/type_hei/reload_alt` |  |
| `event:/infantry/player/weapon/rifle/type_hei_automatic_rifle/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/type_hei_automatic_rifle/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/type_hei_automatic_rifle/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/type_hei_automatic_rifle/reload_mag_punch` |  |
| `event:/infantry/player/weapon/rifle/type_hei_automatic_rifle/reload_mag_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/type_hei_automatic_rifle/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/type_hei_extended/reload` |  |
| `event:/infantry/player/weapon/rifle/type_hei_extended/reload_alt` |  |
| `event:/infantry/player/weapon/rifle/type_hei_late/reload` |  |
| `event:/infantry/player/weapon/rifle/type_hei_late/reload_alt` |  |
| `event:/infantry/player/weapon/rifle/type_i/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/type_i/reload` |  |
| `event:/infantry/player/weapon/rifle/type_ko_rifle/reload_loop_multiple` |  |
| `event:/infantry/player/weapon/rifle/type_ko_rifle/reload_loop_single` |  |
| `event:/infantry/player/weapon/rifle/type_ko_rifle/reload_post` |  |
| `event:/infantry/player/weapon/rifle/type_ko_rifle/reload_prepare` |  |
| `event:/infantry/player/weapon/rifle/vintorez/reload_foley_end` |  |
| `event:/infantry/player/weapon/rifle/vintorez/reload_foley_start` |  |
| `event:/infantry/player/weapon/rifle/vintorez/reload_mag_in` |  |
| `event:/infantry/player/weapon/rifle/vintorez/reload_mag_out` |  |
| `event:/infantry/player/weapon/rifle/vintorez/reload_shutter_in` |  |
| `event:/infantry/player/weapon/rifle/vintorez/reload_shutter_out` |  |
| `event:/infantry/player/weapon/rifle/vstg_1_5/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/vstg_1_5/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/vstg_1_5/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/winchester_1895/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/winchester_1895/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/winchester_1895/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/winchester_1895/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/winchester_1895/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/winchester_1895/reload5/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/winchester_1912/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/winchester_1912/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/winchester_1912/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/winchester_1912/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/winchester_m1907/reload_mag_punch` |  |
| `event:/infantry/player/weapon/rifle/zh_29/bolt_action` |  |
| `event:/infantry/player/weapon/rifle/zh_29/reload1/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/zh_29/reload2/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/zh_29/reload3/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/zh_29/reload4/change_ammo` |  |
| `event:/infantry/player/weapon/rifle/zh_29_jp/reload` |  |
| `event:/infantry/player/weapon/rifle/zh_29_jp/reload_alt` |  |
| `event:/infantry/player/weapon/tnt_block_exploder/activate` |  |
