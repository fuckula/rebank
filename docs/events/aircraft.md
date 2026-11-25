[← Events Index](../EVENTS.md) · [← Docs](../README.md)

# Aircraft — sound events

Aircraft airframes, cockpits, RWR/MLWS alarms, engines, guns and weapons. **10 populated bank(s)** · **2090 named events**.

| Bank | Named events | Waveforms |
| --- | ---: | ---: |
| [`aircraft_ambient`](#aircraft_ambient) | 29 | 197 |
| [`aircraft_common`](#aircraft_common) | 27 | 191 |
| [`aircraft_effects`](#aircraft_effects) | 134 | 742 |
| [`aircraft_engines`](#aircraft_engines) | 1217 | 1358 |
| [`aircraft_gui`](#aircraft_gui) | 310 | 408 |
| [`aircraft_guns`](#aircraft_guns) | 270 | 3162 |
| [`aircraft_music`](#aircraft_music) | 88 | 97 |
| [`aircraft_music_2`](#aircraft_music_2) | 4 | 13 |
| [`aircraft_music_3`](#aircraft_music_3) | 7 | 15 |
| [`aircraft_music_4`](#aircraft_music_4) | 4 | 12 |

## aircraft_ambient

33 events (29 named), 197 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/aircraft/ambient/air_defence_alarm` | Distance |
| `event:/aircraft/ambient/alarm` |  |
| `event:/aircraft/ambient/camp_tanks` | distance |
| `event:/aircraft/ambient/city_01` | distance |
| `event:/aircraft/ambient/explosions` |  |
| `event:/aircraft/ambient/explosions_far` | Distance |
| `event:/aircraft/ambient/global_amb` | storm, nighttime, distance, action, surface |
| `event:/aircraft/ambient/global_amb_arctic` | nighttime, storm, surface, distance, action |
| `event:/aircraft/ambient/global_amb_autumn` | distance, action, surface, storm, nighttime |
| `event:/aircraft/ambient/global_amb_city` | nighttime, storm, surface, distance, action |
| `event:/aircraft/ambient/global_amb_desert` | nighttime, storm, surface, distance, action |
| `event:/aircraft/ambient/global_amb_europe` | storm, nighttime, action, distance, surface |
| `event:/aircraft/ambient/global_amb_tropics` | nighttime, storm, surface, action, distance |
| `event:/aircraft/ambient/global_amb_winter` | storm, nighttime, distance, action, surface |
| `event:/aircraft/ambient/hangar_worldwar` | distance, loop, Direction |
| `event:/aircraft/ambient/launch_far` | Distance |
| `event:/aircraft/ambient/new_hangar/hangar_outside` | Event Cone Angle, nighttime, prem, Distance, height |
| `event:/aircraft/ambient/new_hangar/hangar_outside_halloween` | prem, height, Event Cone Angle, nighttime |
| `event:/aircraft/ambient/new_hangar/hangar_outside_xmas` | nighttime, Event Cone Angle, height, prem |
| `event:/aircraft/ambient/new_hangar/hangar_ships` | Elevation, nighttime, Distance, height, prem, Event Orientation |
| `event:/aircraft/ambient/new_hangar/hangar_ships_halloween` | Event Orientation, prem, height, Distance, Event Cone Angle, nighttime, Elevation |
| `event:/aircraft/ambient/new_hangar/hangar_ships_xmas` | nighttime, Elevation, Event Cone Angle, Distance, height, Event Orientation, prem |
| `event:/aircraft/ambient/new_hangar/hangar_tanks` | nighttime, Event Orientation, prem, height, Distance |
| `event:/aircraft/ambient/new_hangar/hangar_tanks_halloween` | Event Orientation, prem, height, Distance, nighttime |
| `event:/aircraft/ambient/new_hangar/hangar_tanks_xmas` | Event Orientation, prem, height, Distance, Event Cone Angle, nighttime |
| `event:/aircraft/ambient/prelaunch` | Distance, on_shot |
| `event:/aircraft/ambient/prelaunch_ai` | on_shot, Distance |
| `event:/aircraft/ambient/siren` | distance |
| `event:/aircraft/ambient/warfare` | planes, guns |

## aircraft_common

27 events (27 named), 191 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/aircraft/common/bomb_drop` |  |
| `event:/aircraft/common/bomb_hatch` | Distance |
| `event:/aircraft/common/bomb_whistle` | Distance, altitude |
| `event:/aircraft/common/bomb_whistle_ground` | Distance |
| `event:/aircraft/common/engine_fluid_leak` |  |
| `event:/aircraft/common/engine_mf` |  |
| `event:/aircraft/common/engine_mf_jet` |  |
| `event:/aircraft/common/engine_overheat` | overheat, Distance |
| `event:/aircraft/common/engine_overheat_camera` | overheat, Distance |
| `event:/aircraft/common/engine_overheat_cockpit` | overheat |
| `event:/aircraft/common/engine_overheat_start` | Distance, overheat |
| `event:/aircraft/common/redout` |  |
| `event:/aircraft/common/vibration_camera` | overload, speed |
| `event:/aircraft/common/vibration_cockpit` | overload, speed |
| `event:/aircraft/common/vibration_cockpit_open` | airstall, Direction, cockpit_open, speed, overload |
| `event:/aircraft/common/vibration_heli_cockpit_open` | cockpit_open, overload, speed, Direction, airstall |
| `event:/aircraft/common/vibration_heli_land_cockpit` | overload, wheelHit, cockpit_open, is_jet, speed, grass, snow, water |
| `event:/aircraft/common/vibration_jet_cockpit_open` | cockpit_open, speed, overload, Direction, listener_altitude, airstall |
| `event:/aircraft/common/vibration_jet_cockpit_wind` | cockpit_open, overload, speed, listener_altitude, airstall |
| `event:/aircraft/common/vibration_jet_land_cockpit` | water, snow, grass, speed, is_jet, overload, wheelHit, cockpit_open |
| `event:/aircraft/common/vibration_land_camera` | grass, snow, water, wheelHit, overload, speed, Distance |
| `event:/aircraft/common/vibration_land_cockpit` | water, snow, grass, speed, is_jet, overload, wheelHit, cockpit_open |
| `event:/aircraft/common/vibration_overload` | overload |
| `event:/aircraft/common/vibration_wind_heli` | cockpit_open, Distance, speed |
| `event:/aircraft/common/vibration_wind_jet` | speed, cockpit_open, Distance |
| `event:/aircraft/common/vibration_wind_piston` | speed, cockpit_open, Distance |
| `event:/aircraft/engines/engine_wep` | Distance |

## aircraft_effects

172 events (134 named), 742 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/aircraft/common/engine_jet_fluid_leak` |  |
| `event:/aircraft/effects/aerobatics_smoke` | Distance |
| `event:/aircraft/effects/airbrake` | Distance |
| `event:/aircraft/effects/bomb_ground_hit` | Distance |
| `event:/aircraft/effects/bonus` |  |
| `event:/aircraft/effects/bullet_passby` | caliber, velocity |
| `event:/aircraft/effects/bullet_rico_camera` | Distance |
| `event:/aircraft/effects/bullet_rico_cockpit` | Distance |
| `event:/aircraft/effects/bullethit_building` | Distance |
| `event:/aircraft/effects/bullethit_camera` | Distance |
| `event:/aircraft/effects/bullethit_cockpit` | Distance |
| `event:/aircraft/effects/bullethit_cockpit_glass` | Distance |
| `event:/aircraft/effects/bullethit_cockpit_metal` | Distance |
| `event:/aircraft/effects/bullethit_ground` | Distance |
| `event:/aircraft/effects/bullethit_plane` | Distance, is_hit_ours |
| `event:/aircraft/effects/bullethit_plane_he` | is_hit_ours, Distance |
| `event:/aircraft/effects/bullethit_stone` | Distance |
| `event:/aircraft/effects/bullethit_unit` | Distance, is_hit_ours |
| `event:/aircraft/effects/bullethit_water` | Distance |
| `event:/aircraft/effects/bullethit_wood` | Distance |
| `event:/aircraft/effects/chasis` | Distance |
| `event:/aircraft/effects/cockpit` | Distance |
| `event:/aircraft/effects/cockpit_door2_close` | Distance |
| `event:/aircraft/effects/cockpit_door2_open` | Distance |
| `event:/aircraft/effects/cockpit_door3_close` | Distance |
| `event:/aircraft/effects/cockpit_door3_open` | Distance |
| `event:/aircraft/effects/cockpit_door4_close` | Distance |
| `event:/aircraft/effects/cockpit_door_close` | Distance |
| `event:/aircraft/effects/cockpit_door_open` | Distance |
| `event:/aircraft/effects/cockpit_servo` | Distance |
| `event:/aircraft/effects/control_stick` | velocity |
| `event:/aircraft/effects/enemy_explosion` | Distance |
| `event:/aircraft/effects/exhaust` | Distance |
| `event:/aircraft/effects/exhaust_cockpit` |  |
| `event:/aircraft/effects/fire` | Distance, occlusion |
| `event:/aircraft/effects/fire_hangar` | Distance |
| `event:/aircraft/effects/firework` | Distance |
| `event:/aircraft/effects/firework_misc` | Distance |
| `event:/aircraft/effects/fireworks_fountain` | Distance |
| `event:/aircraft/effects/flap` | Distance |
| `event:/aircraft/effects/gripen_passby` | speed, mach, distance |
| `event:/aircraft/effects/ground_collision` | Distance |
| `event:/aircraft/effects/gun_overheat_final` |  |
| `event:/aircraft/effects/gun_overheat_high` |  |
| `event:/aircraft/effects/gun_overheat_low` |  |
| `event:/aircraft/effects/gun_ready` |  |
| `event:/aircraft/effects/gun_turn_manual` | Distance, velH, velV |
| `event:/aircraft/effects/heli_passby` | speed, distance |
| `event:/aircraft/effects/heli_piston_passby` | speed, distance |
| `event:/aircraft/effects/hydraulic_break` | Distance |
| `event:/aircraft/effects/hydroplane` | Distance, engine |
| `event:/aircraft/effects/jet_plane_passby` | mach, speed, distance |
| `event:/aircraft/effects/jump_out_parachute` |  |
| `event:/aircraft/effects/landcrash_smoke` | Distance |
| `event:/aircraft/effects/landing_hook` | Distance |
| `event:/aircraft/effects/light_switch` | Distance |
| `event:/aircraft/effects/low_ground` | distance, speed |
| `event:/aircraft/effects/missile_sonic_boom` | Distance |
| `event:/aircraft/effects/module_damage` | Distance |
| `event:/aircraft/effects/mustang_passby` | speed, distance |
| `event:/aircraft/effects/napalm_spot` | Distance |
| `event:/aircraft/effects/nozzle_moving` | Distance, intensity, listener_altitude |
| `event:/aircraft/effects/nozzle_moving_2` | listener_altitude, intensity, Distance |
| `event:/aircraft/effects/nozzle_moving_3` | listener_altitude, intensity, Distance |
| `event:/aircraft/effects/nozzle_turning` | listener_altitude, intensity, Distance |
| `event:/aircraft/effects/old_ship_hit` | Distance |
| `event:/aircraft/effects/pedals` | velocity |
| `event:/aircraft/effects/pilot_seat_eject` | Distance |
| `event:/aircraft/effects/pilot_seat_rocket` | Distance, Event Cone Angle |
| `event:/aircraft/effects/plane_broken` | Distance |
| `event:/aircraft/effects/plane_fire` | Distance |
| `event:/aircraft/effects/plane_fire_ai` | Distance |
| `event:/aircraft/effects/plane_passby` | distance, speed |
| `event:/aircraft/effects/plane_pieces` | Distance |
| `event:/aircraft/effects/plane_sonic_boom` | Distance, Direction, Elevation, headphones |
| `event:/aircraft/effects/prop_dead` | Distance |
| `event:/aircraft/effects/prop_dead_water` |  |
| `event:/aircraft/effects/rain` | model_type, reverbIndoor, Elevation, mat |
| `event:/aircraft/effects/rain_cockpit` | model_type |
| `event:/aircraft/effects/rocket_passby` | distance |
| `event:/aircraft/effects/stuka_siren` | Speed, Event Cone Angle, Distance, timer |
| `event:/aircraft/effects/stuka_siren_ai` | Event Cone Angle, Elevation, Distance, Speed, headphones, timer, Direction |
| `event:/aircraft/effects/swing_wing` | Distance |
| `event:/aircraft/effects/thrust_lever` | velocity |
| `event:/aircraft/effects/thrust_reverse` | Distance |
| `event:/aircraft/effects/tire_screech` | Distance, speed |
| `event:/aircraft/effects/torpedo_launch` | Distance |
| `event:/aircraft/effects/torpedo_move` | Distance |
| `event:/aircraft/effects/torpedo_splash` | Distance |
| `event:/aircraft/effects/tree_collision` |  |
| `event:/aircraft/effects/tree_creak` |  |
| `event:/aircraft/effects/tree_fall` |  |
| `event:/aircraft/effects/tree_falling` |  |
| `event:/aircraft/effects/turret_turn_servo` | broken, velH, velV, Distance |
| `event:/aircraft/effects/water_collision` |  |
| `event:/aircraft/effects/weapon_trigger` |  |
| `event:/aircraft/effects/wheel_drift` | Distance, surface, speed |
| `event:/aircraft/effects/wind` | speed, distance |
| `event:/aircraft/effects/wreck` | Distance |
| `event:/aircraft/effects/wreck_explosion` | Distance, headphones, Direction |
| `event:/aircraft/effects/wreck_explosion_cockpit` | Distance |
| `event:/aircraft/effects/wreck_scrape` | speed, loop |
| `event:/aircraft/effects/wreck_sinking` | Distance |
| `event:/aircraft/effects/wreck_uav` | Distance, timer |
| `event:/aircraft/explosions/bomb_expl_water_mid` | timer, headphones, Distance, Direction |
| `event:/aircraft/explosions/bomb_expl_water_small` | timer, Distance, headphones, Direction |
| `event:/aircraft/explosions/bomb_explosion_cluster` | timer, Distance, headphones, Direction |
| `event:/aircraft/explosions/bomb_explosion_ground` | Distance, headphones, timer, Direction |
| `event:/aircraft/explosions/bomb_explosion_mid` | Direction, headphones, Distance, timer |
| `event:/aircraft/explosions/bomb_explosion_small` | Direction, headphones, Distance, timer |
| `event:/aircraft/explosions/bomb_explosion_water` | Distance, headphones, timer, Direction |
| `event:/aircraft/explosions/explosion_air` | timer, Distance |
| `event:/aircraft/explosions/explosion_air_small` | Distance, timer |
| `event:/aircraft/explosions/explosion_building` | timer, Distance |
| `event:/aircraft/explosions/explosion_ceramics` | Distance, timer |
| `event:/aircraft/explosions/explosion_ground` | timer, Distance |
| `event:/aircraft/explosions/explosion_naval` | Distance, timer |
| `event:/aircraft/explosions/explosion_unit` | Distance, timer |
| `event:/aircraft/explosions/explosion_water` | timer, Distance |
| `event:/aircraft/explosions/heavy_explosion_air` | Distance, timer |
| `event:/aircraft/explosions/heavy_explosion_building` | timer, Distance |
| `event:/aircraft/explosions/heavy_explosion_ground` | Distance, timer |
| `event:/aircraft/explosions/heavy_explosion_unit` | timer, Distance |
| `event:/aircraft/explosions/heavy_explosion_water` | timer, Distance |
| `event:/aircraft/explosions/misl_explosion_ground` | Distance, timer |
| `event:/aircraft/explosions/misl_explosion_mid` | timer, Distance |
| `event:/aircraft/explosions/misl_explosion_small` | timer, Distance |
| `event:/aircraft/explosions/napaml_explosion` | timer, Distance |
| `event:/aircraft/explosions/napaml_stream` | Distance, timer |
| `event:/aircraft/explosions/parts_explosion` | Distance, timer |
| `event:/aircraft/explosions/parts_explosion_cockpit` | Distance |
| `event:/aircraft/explosions/plane_explosion_water` | Distance, timer |
| `event:/aircraft/explosions/plane_explosion_water_cockpit` | Distance |
| `event:/aircraft/explosions/torpedo_explosion_unit` | Distance, timer |

## aircraft_engines

1222 events (1217 named), 1358 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/aircraft/engines/boat` | Distance, engine |
| `event:/aircraft/engines/engine01` | depth, event_vertical_angle, Distance, zoom, overload, load, Event Cone Angle, rpm |
| `event:/aircraft/engines/engine01_ai` | Elevation, Event Cone Angle, rpm, Distance, load, headphones, is_visible, listener_is_ground, speed_relative, Direction, is_enemy |
| `event:/aircraft/engines/engine01_cockpit_l` | Distance, depth, rpm, cockpit_open, load, overload, zoom |
| `event:/aircraft/engines/engine01_cockpit_r` | rpm, load, cockpit_open, zoom, overload, Distance |
| `event:/aircraft/engines/engine01_prop` | Distance |
| `event:/aircraft/engines/engine01_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine01_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine01_start` | Distance |
| `event:/aircraft/engines/engine01_start_cockpit_l` |  |
| `event:/aircraft/engines/engine01_start_cockpit_r` |  |
| `event:/aircraft/engines/engine01_stop` | Distance |
| `event:/aircraft/engines/engine01_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine01_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine02` | depth, event_vertical_angle, Distance, zoom, overload, load, rpm, Event Cone Angle |
| `event:/aircraft/engines/engine02_ai` | headphones, rpm, Distance, Event Cone Angle, Elevation, load, Direction, is_enemy, is_visible, speed_relative, listener_is_ground |
| `event:/aircraft/engines/engine02_cockpit_l` | depth, Distance, overload, zoom, cockpit_open, load, rpm |
| `event:/aircraft/engines/engine02_cockpit_r` | zoom, overload, rpm, cockpit_open, load, Distance |
| `event:/aircraft/engines/engine02_prop` | Distance |
| `event:/aircraft/engines/engine02_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine02_prop_cockpit_r` | loop, Distance |
| `event:/aircraft/engines/engine02_start` | Distance |
| `event:/aircraft/engines/engine02_start_cockpit_l` |  |
| `event:/aircraft/engines/engine02_start_cockpit_r` |  |
| `event:/aircraft/engines/engine02_stop` | Distance |
| `event:/aircraft/engines/engine02_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine02_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine03` | zoom, overload, load, Event Cone Angle, rpm, event_vertical_angle, depth, Distance |
| `event:/aircraft/engines/engine03_ai` | Elevation, Event Cone Angle, rpm, Distance, load, headphones, is_visible, listener_is_ground, speed_relative, Direction, is_enemy |
| `event:/aircraft/engines/engine03_cockpit_l` | depth, Distance, overload, zoom, cockpit_open, load, rpm |
| `event:/aircraft/engines/engine03_cockpit_r` | Distance, zoom, overload, load, cockpit_open, rpm |
| `event:/aircraft/engines/engine03_prop` | Distance |
| `event:/aircraft/engines/engine03_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine03_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine03_start` | Distance |
| `event:/aircraft/engines/engine03_start_cockpit_l` |  |
| `event:/aircraft/engines/engine03_start_cockpit_r` |  |
| `event:/aircraft/engines/engine03_stop` | Distance |
| `event:/aircraft/engines/engine03_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine03_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine04` | Distance, event_vertical_angle, depth, zoom, overload, Event Cone Angle, rpm, load |
| `event:/aircraft/engines/engine04_ai` | load, rpm, Distance, Elevation, Event Cone Angle, headphones, listener_is_ground, speed_relative, is_visible, is_enemy, Direction |
| `event:/aircraft/engines/engine04_cockpit_l` | Distance, depth, overload, zoom, rpm, load, cockpit_open |
| `event:/aircraft/engines/engine04_cockpit_r` | Distance, load, cockpit_open, rpm, zoom, overload |
| `event:/aircraft/engines/engine04_prop` | Distance |
| `event:/aircraft/engines/engine04_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine04_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine04_start` | Distance |
| `event:/aircraft/engines/engine04_start_cockpit_l` |  |
| `event:/aircraft/engines/engine04_start_cockpit_r` |  |
| `event:/aircraft/engines/engine04_stop` | Distance |
| `event:/aircraft/engines/engine04_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine04_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_02_J33_N1` | overload, zoom, speed, load, rpm, wep, Event Cone Angle, mach, depth, event_vertical_angle, Distance |
| `event:/aircraft/engines/engine05_02_J33_N1_cockpit_l` | depth, wep, rpm, cockpit_open, Distance, load, zoom, overload |
| `event:/aircraft/engines/engine05_02_J33_N1_cockpit_r` | rpm, wep, load, Distance, cockpit_open, zoom, overload |
| `event:/aircraft/engines/engine05_02_J33_N1_start` | Distance |
| `event:/aircraft/engines/engine05_02_J33_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_02_J33_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_02_J33_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_02_J33_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_02_J33_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_02_dervent_N1` | Distance, mach, event_vertical_angle, depth, speed, overload, zoom, wep, rpm, Event Cone Angle, load |
| `event:/aircraft/engines/engine05_02_dervent_N1_ai` | headphones, Elevation, Event Cone Angle, Distance, load, Direction, is_enemy, rpm, is_visible, depth, speed_relative, mach |
| `event:/aircraft/engines/engine05_02_dervent_N1_cockpit_l` | wep, rpm, load, cockpit_open, Distance, overload, zoom, depth |
| `event:/aircraft/engines/engine05_02_dervent_N1_cockpit_r` | rpm, wep, Distance, cockpit_open, load, overload, zoom |
| `event:/aircraft/engines/engine05_02_dervent_N1_start` | Distance |
| `event:/aircraft/engines/engine05_02_dervent_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_02_dervent_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_02_dervent_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_02_dervent_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_02_dervent_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_02_dervent_twin_N1` | Event Cone Angle, wep, rpm, load, speed, overload, zoom, Distance, event_vertical_angle, depth, mach |
| `event:/aircraft/engines/engine05_02_dervent_twin_N1_ai` | is_visible, depth, speed_relative, mach, Direction, is_enemy, rpm, Elevation, Event Cone Angle, Distance, load, headphones |
| `event:/aircraft/engines/engine05_02_dervent_twin_N1_start` | Distance |
| `event:/aircraft/engines/engine05_02_dervent_twin_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_02_goblin_N1` | overload, zoom, speed, load, Event Cone Angle, wep, rpm, depth, event_vertical_angle, mach, Distance |
| `event:/aircraft/engines/engine05_02_goblin_N1_WEP` | load, Event Cone Angle, rpm, wep, zoom, overload, speed, event_vertical_angle, depth, mach, Distance |
| `event:/aircraft/engines/engine05_02_goblin_N1_WEP_ai` | headphones, Event Cone Angle, Elevation, Distance, load, Direction, is_enemy, rpm, is_visible, speed_relative, depth, mach |
| `event:/aircraft/engines/engine05_02_goblin_N1_WEP_cockpit_l` | zoom, overload, load, cockpit_open, Distance, wep, rpm, depth |
| `event:/aircraft/engines/engine05_02_goblin_N1_WEP_cockpit_r` | zoom, overload, load, Distance, cockpit_open, rpm, wep |
| `event:/aircraft/engines/engine05_02_goblin_N1_cockpit_l` | depth, zoom, overload, load, Distance, cockpit_open, rpm, wep |
| `event:/aircraft/engines/engine05_02_goblin_N1_cockpit_r` | zoom, overload, rpm, wep, load, Distance, cockpit_open |
| `event:/aircraft/engines/engine05_02_goblin_N1_start` | Distance |
| `event:/aircraft/engines/engine05_02_goblin_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_02_goblin_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_02_goblin_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_02_goblin_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_02_goblin_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_02_nene_N1` | mach, depth, event_vertical_angle, Distance, overload, zoom, speed, load, rpm, wep, Event Cone Angle |
| `event:/aircraft/engines/engine05_02_nene_N1_WEP` | mach, event_vertical_angle, depth, Distance, load, wep, rpm, Event Cone Angle, zoom, overload, speed |
| `event:/aircraft/engines/engine05_02_nene_N1_WEP_ai` | Direction, rpm, is_enemy, is_visible, speed_relative, depth, mach, headphones, Event Cone Angle, Elevation, Distance, load |
| `event:/aircraft/engines/engine05_02_nene_N1_WEP_cockpit_l` | zoom, overload, load, Distance, cockpit_open, rpm, wep, depth |
| `event:/aircraft/engines/engine05_02_nene_N1_WEP_cockpit_r` | load, Distance, cockpit_open, rpm, wep, overload, zoom |
| `event:/aircraft/engines/engine05_02_nene_N1_ai` | speed_relative, depth, mach, is_visible, is_enemy, rpm, Direction, load, Event Cone Angle, Elevation, Distance, headphones |
| `event:/aircraft/engines/engine05_02_nene_N1_cockpit_l` | depth, load, cockpit_open, Distance, wep, rpm, zoom, overload |
| `event:/aircraft/engines/engine05_02_nene_N1_cockpit_r` | wep, rpm, load, cockpit_open, Distance, overload, zoom |
| `event:/aircraft/engines/engine05_02_nene_N1_start` | Distance |
| `event:/aircraft/engines/engine05_02_nene_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_02_nene_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_02_nene_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_02_nene_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_02_nene_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_04_J79GE_N1_WEP` | speed, zoom, overload, Event Cone Angle, wep, load, Distance, event_vertical_angle, depth, mach, rpm |
| `event:/aircraft/engines/engine05_04_J79GE_N1_WEP_ai` | headphones, Distance, Event Cone Angle, Elevation, load, Direction, is_enemy, rpm, is_visible, mach, speed_relative, depth |
| `event:/aircraft/engines/engine05_04_J79GE_N1_WEP_cockpit_l` | overload, zoom, wep, cockpit_open, Distance, load, depth, rpm |
| `event:/aircraft/engines/engine05_04_J79GE_N1_WEP_cockpit_r` | overload, zoom, wep, load, cockpit_open, Distance, rpm |
| `event:/aircraft/engines/engine05_04_J79GE_N1_start` | Distance |
| `event:/aircraft/engines/engine05_04_J79GE_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_04_J79GE_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_04_J79GE_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_04_J79GE_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_04_J79GE_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_04_Jumo004_N1` | Distance, depth, event_vertical_angle, mach, speed, zoom, overload, Event Cone Angle, wep, rpm, load |
| `event:/aircraft/engines/engine05_04_Jumo004_N1_ai` | Direction, is_enemy, rpm, is_visible, speed_relative, depth, mach, headphones, Event Cone Angle, Elevation, Distance, load |
| `event:/aircraft/engines/engine05_04_Jumo004_N1_cockpit_l` | depth, wep, rpm, cockpit_open, Distance, load, zoom, overload |
| `event:/aircraft/engines/engine05_04_Jumo004_N1_cockpit_r` | wep, rpm, cockpit_open, Distance, load, zoom, overload |
| `event:/aircraft/engines/engine05_04_Jumo004_N1_start` | Distance |
| `event:/aircraft/engines/engine05_04_Jumo004_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_04_Jumo004_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_04_Jumo004_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_04_Jumo004_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_04_Jumo004_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_04_Jumo004_twin_N1` | speed, zoom, overload, rpm, wep, Event Cone Angle, load, Distance, mach, event_vertical_angle, depth |
| `event:/aircraft/engines/engine05_04_Jumo004_twin_N1_start` | Distance |
| `event:/aircraft/engines/engine05_04_Jumo004_twin_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_05_J79_N1` | overload, zoom, speed, load, wep, rpm, Event Cone Angle, mach, depth, event_vertical_angle, Distance |
| `event:/aircraft/engines/engine05_05_J79_N1_ai` | Elevation, Event Cone Angle, Distance, load, headphones, is_visible, depth, speed_relative, mach, Direction, rpm, is_enemy |
| `event:/aircraft/engines/engine05_05_J79_N1_cockpit_l` | load, cockpit_open, Distance, wep, rpm, overload, zoom, depth |
| `event:/aircraft/engines/engine05_05_J79_N1_cockpit_r` | overload, zoom, rpm, wep, Distance, cockpit_open, load |
| `event:/aircraft/engines/engine05_05_J79_N1_start` | Distance |
| `event:/aircraft/engines/engine05_05_J79_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_05_J79_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_05_J79_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_05_J79_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_05_J79_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_06_J47_N1` | Distance, mach, event_vertical_angle, depth, rpm, wep, Event Cone Angle, load, speed, zoom, overload |
| `event:/aircraft/engines/engine05_06_J47_N1_WEP` | load, Event Cone Angle, rpm, wep, zoom, overload, speed, depth, event_vertical_angle, mach, Distance |
| `event:/aircraft/engines/engine05_06_J47_N1_WEP_ai` | headphones, load, Event Cone Angle, Elevation, Distance, is_enemy, rpm, Direction, speed_relative, depth, mach, is_visible |
| `event:/aircraft/engines/engine05_06_J47_N1_WEP_cockpit_l` | zoom, overload, rpm, wep, Distance, cockpit_open, load, depth |
| `event:/aircraft/engines/engine05_06_J47_N1_WEP_cockpit_r` | Distance, cockpit_open, load, rpm, wep, overload, zoom |
| `event:/aircraft/engines/engine05_06_J47_N1_ai` | is_visible, mach, speed_relative, depth, Direction, rpm, is_enemy, Distance, Event Cone Angle, Elevation, load, headphones |
| `event:/aircraft/engines/engine05_06_J47_N1_cockpit_l` | rpm, wep, load, Distance, cockpit_open, overload, zoom, depth |
| `event:/aircraft/engines/engine05_06_J47_N1_cockpit_r` | wep, rpm, load, cockpit_open, Distance, overload, zoom |
| `event:/aircraft/engines/engine05_06_J47_N1_start` | Distance |
| `event:/aircraft/engines/engine05_06_J47_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_06_J47_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_06_J47_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_06_J47_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_06_J47_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_06_J65W_N1` | mach, event_vertical_angle, depth, Distance, load, wep, rpm, Event Cone Angle, zoom, overload, speed |
| `event:/aircraft/engines/engine05_06_J65W_N1_WEP` | speed, overload, zoom, wep, rpm, Event Cone Angle, load, Distance, mach, event_vertical_angle, depth |
| `event:/aircraft/engines/engine05_06_J65W_N1_WEP_ai` | headphones, Distance, Event Cone Angle, Elevation, load, Direction, rpm, is_enemy, is_visible, mach, speed_relative, depth |
| `event:/aircraft/engines/engine05_06_J65W_N1_WEP_cockpit_l` | Distance, cockpit_open, load, rpm, wep, zoom, overload, depth |
| `event:/aircraft/engines/engine05_06_J65W_N1_WEP_cockpit_r` | wep, rpm, cockpit_open, Distance, load, zoom, overload |
| `event:/aircraft/engines/engine05_06_J65W_N1_ai` | load, Distance, Event Cone Angle, Elevation, headphones, mach, speed_relative, depth, is_visible, rpm, is_enemy, Direction |
| `event:/aircraft/engines/engine05_06_J65W_N1_cockpit_l` | depth, zoom, overload, cockpit_open, Distance, load, wep, rpm |
| `event:/aircraft/engines/engine05_06_J65W_N1_cockpit_r` | load, cockpit_open, Distance, wep, rpm, overload, zoom |
| `event:/aircraft/engines/engine05_06_J65W_N1_start` | Distance |
| `event:/aircraft/engines/engine05_06_J65W_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_06_J65W_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_06_J65W_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_06_J65W_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_06_J65W_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_06_avon_N1_N2` | speed, zoom, overload, rpm, wep, Event Cone Angle, load, Distance, mach, depth, event_vertical_angle |
| `event:/aircraft/engines/engine05_06_avon_N1_N2_ai` | mach, speed_relative, depth, is_visible, rpm, is_enemy, Direction, load, Distance, Event Cone Angle, Elevation, headphones |
| `event:/aircraft/engines/engine05_06_avon_N1_N2_cockpit_l` | wep, rpm, load, cockpit_open, Distance, overload, zoom, depth |
| `event:/aircraft/engines/engine05_06_avon_N1_N2_cockpit_r` | cockpit_open, Distance, load, wep, rpm, zoom, overload |
| `event:/aircraft/engines/engine05_06_avon_N1_N2_hunter` | zoom, overload, speed, load, wep, rpm, Event Cone Angle, mach, event_vertical_angle, depth, Distance |
| `event:/aircraft/engines/engine05_06_avon_N1_N2_hunter_ai` | is_visible, depth, speed_relative, mach, Direction, is_enemy, rpm, Elevation, Event Cone Angle, Distance, load, headphones |
| `event:/aircraft/engines/engine05_06_avon_N1_start` | Distance |
| `event:/aircraft/engines/engine05_06_avon_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_06_avon_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_06_avon_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_06_avon_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_06_avon_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_06_avon_twin_N1_N2` | mach, depth, event_vertical_angle, Distance, load, wep, rpm, Event Cone Angle, zoom, overload, speed |
| `event:/aircraft/engines/engine05_06_avon_twin_N1_start` | Distance |
| `event:/aircraft/engines/engine05_06_avon_twin_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_06_spey_N1_N2` | Distance, mach, depth, event_vertical_angle, speed, zoom, overload, wep, rpm, Event Cone Angle, load |
| `event:/aircraft/engines/engine05_06_spey_N1_N2_ai` | Direction, rpm, is_enemy, is_visible, speed_relative, depth, mach, headphones, Event Cone Angle, Elevation, Distance, load |
| `event:/aircraft/engines/engine05_06_spey_N1_N2_cockpit_l` | overload, zoom, rpm, wep, Distance, cockpit_open, load, depth |
| `event:/aircraft/engines/engine05_06_spey_N1_N2_cockpit_r` | zoom, overload, Distance, cockpit_open, load, rpm, wep |
| `event:/aircraft/engines/engine05_06_spey_N1_start` | Distance |
| `event:/aircraft/engines/engine05_06_spey_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_06_spey_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_06_spey_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_06_spey_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_06_spey_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_06_spey_twin_N1_N2` | load, Event Cone Angle, wep, rpm, zoom, overload, speed, event_vertical_angle, depth, mach, Distance |
| `event:/aircraft/engines/engine05_06_spey_twin_N1_start` | Distance |
| `event:/aircraft/engines/engine05_06_spey_twin_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_J34WE_N1` | overload, zoom, speed, load, Event Cone Angle, rpm, wep, event_vertical_angle, depth, mach, Distance |
| `event:/aircraft/engines/engine05_J34WE_N1_ai` | headphones, load, Event Cone Angle, Elevation, Distance, rpm, is_enemy, Direction, speed_relative, depth, mach, is_visible |
| `event:/aircraft/engines/engine05_J34WE_N1_cockpit_l` | zoom, overload, rpm, wep, Distance, cockpit_open, load, depth |
| `event:/aircraft/engines/engine05_J34WE_N1_cockpit_r` | wep, rpm, load, cockpit_open, Distance, zoom, overload |
| `event:/aircraft/engines/engine05_J34WE_N1_start` | Distance |
| `event:/aircraft/engines/engine05_J34WE_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_J34WE_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_J34WE_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_J34WE_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_J34WE_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_J52` | depth, event_vertical_angle, mach, Distance, overload, zoom, speed, load, Event Cone Angle, rpm, wep |
| `event:/aircraft/engines/engine05_J52P_N1` | mach, depth, event_vertical_angle, Distance, load, rpm, wep, Event Cone Angle, zoom, overload, speed |
| `event:/aircraft/engines/engine05_J52P_N1_ai` | Direction, rpm, is_enemy, is_visible, mach, depth, speed_relative, headphones, Distance, Elevation, Event Cone Angle, load |
| `event:/aircraft/engines/engine05_J52P_N1_cockpit_l` | load, Distance, cockpit_open, rpm, wep, overload, zoom, depth |
| `event:/aircraft/engines/engine05_J52P_N1_cockpit_r` | overload, zoom, wep, rpm, cockpit_open, Distance, load |
| `event:/aircraft/engines/engine05_J52P_N1_start` | Distance |
| `event:/aircraft/engines/engine05_J52P_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_J52P_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_J52P_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_J52P_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_J52P_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_J52_ai` | headphones, load, Event Cone Angle, Elevation, Distance, rpm, is_enemy, Direction, speed_relative, depth, mach, is_visible |
| `event:/aircraft/engines/engine05_J52_cockpit_l` | overload, zoom, Distance, cockpit_open, load, rpm, wep, depth |
| `event:/aircraft/engines/engine05_J52_cockpit_r` | zoom, overload, load, Distance, cockpit_open, rpm, wep |
| `event:/aircraft/engines/engine05_J52_start` | Distance |
| `event:/aircraft/engines/engine05_J52_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_J52_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_J52_stop` | Distance |
| `event:/aircraft/engines/engine05_J52_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_J52_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_J57P_N1_WEP` | depth, event_vertical_angle, mach, Distance, load, Event Cone Angle, rpm, wep, zoom, overload, speed |
| `event:/aircraft/engines/engine05_J57P_N1_WEP_ai` | Event Cone Angle, Elevation, Distance, load, headphones, is_visible, speed_relative, depth, mach, Direction, is_enemy, rpm |
| `event:/aircraft/engines/engine05_J57P_N1_WEP_cockpit_l` | wep, rpm, cockpit_open, Distance, load, overload, zoom, depth |
| `event:/aircraft/engines/engine05_J57P_N1_WEP_cockpit_r` | wep, rpm, cockpit_open, Distance, load, overload, zoom |
| `event:/aircraft/engines/engine05_J57P_N1_start` | Distance |
| `event:/aircraft/engines/engine05_J57P_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_J57P_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_J57P_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_J57P_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_J57P_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_J85_N1` | Event Cone Angle, rpm, wep, load, speed, zoom, overload, Distance, depth, event_vertical_angle, mach |
| `event:/aircraft/engines/engine05_J85_N1_WEP` | Distance, mach, event_vertical_angle, depth, rpm, wep, Event Cone Angle, load, speed, overload, zoom |
| `event:/aircraft/engines/engine05_J85_N1_WEP_ai` | headphones, Distance, Event Cone Angle, Elevation, load, Direction, is_enemy, rpm, is_visible, mach, speed_relative, depth |
| `event:/aircraft/engines/engine05_J85_N1_WEP_cockpit_l` | depth, overload, zoom, rpm, wep, load, Distance, cockpit_open |
| `event:/aircraft/engines/engine05_J85_N1_WEP_cockpit_r` | load, Distance, cockpit_open, rpm, wep, zoom, overload |
| `event:/aircraft/engines/engine05_J85_N1_ai` | Direction, is_enemy, rpm, is_visible, mach, depth, speed_relative, headphones, Distance, Elevation, Event Cone Angle, load |
| `event:/aircraft/engines/engine05_J85_N1_cockpit_l` | depth, overload, zoom, rpm, wep, load, Distance, cockpit_open |
| `event:/aircraft/engines/engine05_J85_N1_cockpit_r` | overload, zoom, rpm, wep, load, Distance, cockpit_open |
| `event:/aircraft/engines/engine05_J85_N1_start` | Distance |
| `event:/aircraft/engines/engine05_J85_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_J85_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_J85_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_J85_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_J85_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_TF30_N1_WEP` | load, Event Cone Angle, wep, zoom, overload, speed, event_vertical_angle, depth, mach, rpm, Distance |
| `event:/aircraft/engines/engine05_TF30_N1_WEP_ai` | Direction, rpm, is_enemy, is_visible, speed_relative, depth, mach, headphones, Event Cone Angle, Elevation, Distance, load |
| `event:/aircraft/engines/engine05_TF30_N1_WEP_cockpit_l` | cockpit_open, Distance, load, wep, overload, zoom, depth, rpm |
| `event:/aircraft/engines/engine05_TF30_N1_WEP_cockpit_r` | rpm, zoom, overload, cockpit_open, Distance, load, wep |
| `event:/aircraft/engines/engine05_TF30_N1_start` | Distance |
| `event:/aircraft/engines/engine05_TF30_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_TF30_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_TF30_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_TF30_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_TF30_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_TF34_N1` | mach, depth, event_vertical_angle, Distance, zoom, overload, speed, load, rpm, wep, rpm_result_tf34, Event Cone Angle |
| `event:/aircraft/engines/engine05_TF34_N1_ai` | Direction, rpm, is_enemy, is_visible, mach, speed_relative, depth, headphones, Distance, Event Cone Angle, Elevation, load |
| `event:/aircraft/engines/engine05_TF34_N1_cockpit_l` | zoom, overload, load, cockpit_open, Distance, rpm_result_tf34, wep, rpm, depth |
| `event:/aircraft/engines/engine05_TF34_N1_cockpit_r` | load, Distance, cockpit_open, rpm, wep, rpm_result_tf34, zoom, overload |
| `event:/aircraft/engines/engine05_TF34_N1_start` | Distance |
| `event:/aircraft/engines/engine05_TF34_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_TF34_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_TF34_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_TF34_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_TF34_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_TF40_N1` | overload, zoom, speed, load, Event Cone Angle, wep, rpm, depth, event_vertical_angle, mach, Distance |
| `event:/aircraft/engines/engine05_TF40_N1_WEP` | Distance, mach, depth, event_vertical_angle, speed, zoom, overload, wep, rpm, Event Cone Angle, load |
| `event:/aircraft/engines/engine05_TF40_N1_WEP_ai` | rpm, is_enemy, Direction, depth, speed_relative, mach, is_visible, headphones, load, Elevation, Event Cone Angle, Distance |
| `event:/aircraft/engines/engine05_TF40_N1_WEP_cockpit_l` | overload, zoom, rpm, wep, Distance, cockpit_open, load, depth |
| `event:/aircraft/engines/engine05_TF40_N1_WEP_cockpit_r` | load, cockpit_open, Distance, wep, rpm, overload, zoom |
| `event:/aircraft/engines/engine05_TF40_N1_ai` | is_visible, speed_relative, depth, mach, Direction, is_enemy, rpm, Event Cone Angle, Elevation, Distance, load, headphones |
| `event:/aircraft/engines/engine05_TF40_N1_cockpit_l` | depth, load, Distance, cockpit_open, rpm, wep, overload, zoom |
| `event:/aircraft/engines/engine05_TF40_N1_cockpit_r` | load, Distance, cockpit_open, rpm, wep, zoom, overload |
| `event:/aircraft/engines/engine05_TF40_N1_start` | Distance |
| `event:/aircraft/engines/engine05_TF40_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_TF40_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_TF40_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_TF40_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_TF40_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_TF41_N1` | Distance, event_vertical_angle, depth, mach, speed, overload, zoom, Event Cone Angle, rpm, wep, load |
| `event:/aircraft/engines/engine05_TF41_N1_ai` | is_visible, speed_relative, depth, mach, Direction, rpm, is_enemy, Event Cone Angle, Elevation, Distance, load, headphones |
| `event:/aircraft/engines/engine05_TF41_N1_cockpit_l` | depth, zoom, overload, wep, rpm, load, cockpit_open, Distance |
| `event:/aircraft/engines/engine05_TF41_N1_cockpit_r` | load, cockpit_open, Distance, wep, rpm, zoom, overload |
| `event:/aircraft/engines/engine05_TF41_N1_start` | Distance |
| `event:/aircraft/engines/engine05_TF41_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_TF41_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_TF41_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_TF41_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_TF41_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_aL21_N1` | overload, zoom, speed, load, wep, rpm, Event Cone Angle, mach, depth, event_vertical_angle, Distance |
| `event:/aircraft/engines/engine05_aL21_N1_WEP` | depth, event_vertical_angle, mach, Distance, load, Event Cone Angle, rpm, wep, overload, zoom, speed |
| `event:/aircraft/engines/engine05_aL21_N1_WEP_ai` | Direction, is_enemy, rpm, is_visible, depth, speed_relative, mach, headphones, Elevation, Event Cone Angle, Distance, load |
| `event:/aircraft/engines/engine05_aL21_N1_WEP_cockpit_l` | zoom, overload, wep, rpm, cockpit_open, Distance, load, depth |
| `event:/aircraft/engines/engine05_aL21_N1_WEP_cockpit_r` | overload, zoom, Distance, cockpit_open, load, rpm, wep |
| `event:/aircraft/engines/engine05_aL21_N1_ai` | rpm, is_enemy, Direction, mach, speed_relative, depth, is_visible, headphones, load, Distance, Event Cone Angle, Elevation |
| `event:/aircraft/engines/engine05_aL21_N1_cockpit_l` | depth, rpm, wep, load, Distance, cockpit_open, overload, zoom |
| `event:/aircraft/engines/engine05_aL21_N1_cockpit_r` | load, Distance, cockpit_open, rpm, wep, zoom, overload |
| `event:/aircraft/engines/engine05_aL21_N1_start` | Distance |
| `event:/aircraft/engines/engine05_aL21_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_aL21_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_aL21_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_aL21_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_aL21_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_aL_31f_WEP` | mach, rpm, event_vertical_angle, depth, Distance, load, wep, Event Cone Angle, overload, zoom, speed |
| `event:/aircraft/engines/engine05_aL_31f_WEP_ai` | Direction, rpm, is_enemy, is_visible, mach, speed_relative, depth, headphones, Distance, Event Cone Angle, Elevation, load |
| `event:/aircraft/engines/engine05_aL_31f_WEP_cockpit_l` | zoom, overload, load, Distance, cockpit_open, wep, rpm, depth |
| `event:/aircraft/engines/engine05_aL_31f_WEP_cockpit_r` | rpm, load, Distance, cockpit_open, wep, zoom, overload |
| `event:/aircraft/engines/engine05_aL_31f_start` | Distance |
| `event:/aircraft/engines/engine05_aL_31f_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_aL_31f_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_aL_31f_stop` | Distance |
| `event:/aircraft/engines/engine05_aL_31f_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_aL_31f_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_aero_rm12_WEP` | depth, event_vertical_angle, mach, rpm, Distance, zoom, overload, speed, load, Event Cone Angle, wep |
| `event:/aircraft/engines/engine05_aero_rm12_WEP_ai` | headphones, Elevation, Event Cone Angle, Distance, load, Direction, is_enemy, rpm, is_visible, depth, speed_relative, mach |
| `event:/aircraft/engines/engine05_aero_rm12_WEP_cockpit_l` | rpm, depth, wep, load, Distance, cockpit_open, overload, zoom |
| `event:/aircraft/engines/engine05_aero_rm12_WEP_cockpit_r` | overload, zoom, load, Distance, cockpit_open, wep, rpm |
| `event:/aircraft/engines/engine05_aero_rm12_start` | Distance |
| `event:/aircraft/engines/engine05_aero_rm12_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_aero_rm12_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_aero_rm12_stop` | Distance |
| `event:/aircraft/engines/engine05_aero_rm12_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_aero_rm12_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_ai25tl` | Distance, depth, event_vertical_angle, mach, Event Cone Angle, rpm, wep, load, speed, overload, zoom |
| `event:/aircraft/engines/engine05_ai25tl_ai` | Distance, Event Cone Angle, Elevation, load, headphones, is_visible, mach, speed_relative, depth, Direction, is_enemy, rpm |
| `event:/aircraft/engines/engine05_ai25tl_cockpit_l` | depth, overload, zoom, cockpit_open, Distance, load, wep, rpm |
| `event:/aircraft/engines/engine05_ai25tl_cockpit_r` | wep, rpm, cockpit_open, Distance, load, zoom, overload |
| `event:/aircraft/engines/engine05_ai25tl_start` | Distance |
| `event:/aircraft/engines/engine05_ai25tl_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_ai25tl_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_ai25tl_stop` | Distance |
| `event:/aircraft/engines/engine05_ai25tl_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_ai25tl_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_atar_N1` | depth, event_vertical_angle, mach, Distance, load, Event Cone Angle, wep, rpm, overload, zoom, speed |
| `event:/aircraft/engines/engine05_atar_N1_WEP` | mach, event_vertical_angle, depth, Distance, load, rpm, wep, Event Cone Angle, overload, zoom, speed |
| `event:/aircraft/engines/engine05_atar_N1_WEP_ai` | mach, depth, speed_relative, is_visible, rpm, is_enemy, Direction, load, Distance, Elevation, Event Cone Angle, headphones |
| `event:/aircraft/engines/engine05_atar_N1_WEP_cockpit_l` | rpm, wep, Distance, cockpit_open, load, zoom, overload, depth |
| `event:/aircraft/engines/engine05_atar_N1_WEP_cockpit_r` | load, Distance, cockpit_open, rpm, wep, overload, zoom |
| `event:/aircraft/engines/engine05_atar_N1_ai` | Direction, rpm, is_enemy, is_visible, mach, depth, speed_relative, headphones, Distance, Elevation, Event Cone Angle, load |
| `event:/aircraft/engines/engine05_atar_N1_cockpit_l` | depth, zoom, overload, Distance, cockpit_open, load, rpm, wep |
| `event:/aircraft/engines/engine05_atar_N1_cockpit_r` | wep, rpm, load, cockpit_open, Distance, overload, zoom |
| `event:/aircraft/engines/engine05_atar_N1_start` | Distance |
| `event:/aircraft/engines/engine05_atar_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_atar_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_atar_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_atar_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_atar_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_ej200_WEP` | Distance, depth, event_vertical_angle, rpm, mach, Event Cone Angle, wep, load, speed, zoom, overload |
| `event:/aircraft/engines/engine05_ej200_WEP_ai` | Distance, Event Cone Angle, Elevation, load, headphones, is_visible, mach, speed_relative, depth, Direction, is_enemy, rpm |
| `event:/aircraft/engines/engine05_ej200_WEP_cockpit_l` | rpm, depth, zoom, overload, wep, load, Distance, cockpit_open |
| `event:/aircraft/engines/engine05_ej200_WEP_cockpit_r` | rpm, wep, load, cockpit_open, Distance, zoom, overload |
| `event:/aircraft/engines/engine05_ej200_start` | Distance |
| `event:/aircraft/engines/engine05_ej200_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_ej200_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_ej200_stop` | Distance |
| `event:/aircraft/engines/engine05_ej200_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_ej200_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_f100_pw_100_WEP` | zoom, overload, speed, load, wep, Event Cone Angle, rpm, mach, event_vertical_angle, depth, Distance |
| `event:/aircraft/engines/engine05_f100_pw_100_WEP_ai` | headphones, load, Distance, Event Cone Angle, Elevation, rpm, is_enemy, Direction, mach, speed_relative, depth, is_visible |
| `event:/aircraft/engines/engine05_f100_pw_100_WEP_cockpit_l` | rpm, depth, overload, zoom, load, cockpit_open, Distance, wep |
| `event:/aircraft/engines/engine05_f100_pw_100_WEP_cockpit_r` | wep, load, Distance, cockpit_open, overload, zoom, rpm |
| `event:/aircraft/engines/engine05_f100_pw_100_start` | Distance |
| `event:/aircraft/engines/engine05_f100_pw_100_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_f100_pw_100_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_f100_pw_100_stop` | Distance |
| `event:/aircraft/engines/engine05_f100_pw_100_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_f100_pw_100_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_f110_WEP` | wep, Event Cone Angle, load, speed, overload, zoom, Distance, rpm, mach, event_vertical_angle, depth |
| `event:/aircraft/engines/engine05_f110_WEP_ai` | Direction, is_enemy, rpm, is_visible, depth, speed_relative, mach, headphones, Elevation, Event Cone Angle, Distance, load |
| `event:/aircraft/engines/engine05_f110_WEP_cockpit_l` | Distance, cockpit_open, load, wep, overload, zoom, depth, rpm |
| `event:/aircraft/engines/engine05_f110_WEP_cockpit_r` | rpm, wep, cockpit_open, Distance, load, zoom, overload |
| `event:/aircraft/engines/engine05_f110_start` | Distance |
| `event:/aircraft/engines/engine05_f110_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_f110_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_f110_stop` | Distance |
| `event:/aircraft/engines/engine05_f110_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_f110_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_f404_WEP` | Distance, depth, event_vertical_angle, mach, rpm, Event Cone Angle, wep, load, speed, zoom, overload |
| `event:/aircraft/engines/engine05_f404_WEP_ai` | Event Cone Angle, Elevation, Distance, load, headphones, is_visible, speed_relative, depth, mach, Direction, is_enemy, rpm |
| `event:/aircraft/engines/engine05_f404_WEP_cockpit_l` | rpm, depth, wep, load, Distance, cockpit_open, zoom, overload |
| `event:/aircraft/engines/engine05_f404_WEP_cockpit_r` | rpm, overload, zoom, load, cockpit_open, Distance, wep |
| `event:/aircraft/engines/engine05_f404_start` | Distance |
| `event:/aircraft/engines/engine05_f404_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_f404_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_f404_stop` | Distance |
| `event:/aircraft/engines/engine05_f404_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_f404_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_m53_p2` | load, Event Cone Angle, rpm, wep, zoom, overload, speed, depth, event_vertical_angle, mach, Distance |
| `event:/aircraft/engines/engine05_m53_p2_ai` | Direction, is_enemy, rpm, is_visible, speed_relative, depth, mach, headphones, Event Cone Angle, Elevation, Distance, load |
| `event:/aircraft/engines/engine05_m53_p2_cockpit_l` | depth, overload, zoom, cockpit_open, Distance, load, wep, rpm |
| `event:/aircraft/engines/engine05_m53_p2_cockpit_r` | cockpit_open, Distance, load, wep, rpm, zoom, overload |
| `event:/aircraft/engines/engine05_m53_p2_start` | Distance |
| `event:/aircraft/engines/engine05_m53_p2_stop` | Distance |
| `event:/aircraft/engines/engine05_m882_WEP` | Distance, rpm, mach, depth, event_vertical_angle, speed, zoom, overload, wep, Event Cone Angle, load |
| `event:/aircraft/engines/engine05_m882_WEP_ai` | headphones, Distance, Event Cone Angle, Elevation, load, Direction, is_enemy, rpm, is_visible, mach, speed_relative, depth |
| `event:/aircraft/engines/engine05_m882_WEP_cockpit_l` | zoom, overload, wep, cockpit_open, Distance, load, depth, rpm |
| `event:/aircraft/engines/engine05_m882_WEP_cockpit_r` | cockpit_open, Distance, load, wep, overload, zoom, rpm |
| `event:/aircraft/engines/engine05_m882_start` | Distance |
| `event:/aircraft/engines/engine05_m882_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_m882_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_m882_stop` | Distance |
| `event:/aircraft/engines/engine05_m882_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_m882_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_pegasus_N1` | speed, zoom, overload, Event Cone Angle, rpm, wep, load, Distance, depth, event_vertical_angle, mach |
| `event:/aircraft/engines/engine05_pegasus_N1_ai` | headphones, load, Distance, Event Cone Angle, Elevation, rpm, is_enemy, Direction, mach, speed_relative, depth, is_visible |
| `event:/aircraft/engines/engine05_pegasus_N1_cockpit_l` | depth, rpm, wep, Distance, cockpit_open, load, zoom, overload |
| `event:/aircraft/engines/engine05_pegasus_N1_cockpit_r` | wep, rpm, load, cockpit_open, Distance, overload, zoom |
| `event:/aircraft/engines/engine05_pegasus_N1_start` | Distance |
| `event:/aircraft/engines/engine05_pegasus_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_pegasus_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_pegasus_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_pegasus_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_pegasus_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_r11_N1_WEP` | overload, zoom, speed, load, rpm, wep, Event Cone Angle, mach, depth, event_vertical_angle, Distance |
| `event:/aircraft/engines/engine05_r11_N1_WEP_ai` | rpm, is_enemy, Direction, speed_relative, depth, mach, is_visible, headphones, load, Event Cone Angle, Elevation, Distance |
| `event:/aircraft/engines/engine05_r11_N1_WEP_cockpit_l` | cockpit_open, Distance, load, wep, rpm, overload, zoom, depth |
| `event:/aircraft/engines/engine05_r11_N1_WEP_cockpit_r` | overload, zoom, cockpit_open, Distance, load, wep, rpm |
| `event:/aircraft/engines/engine05_r11_N1_start` | Distance |
| `event:/aircraft/engines/engine05_r11_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_r11_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_r11_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_r11_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_r11_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_r15B300_WEP` | Event Cone Angle, wep, rpm, load, speed, overload, zoom, Distance, event_vertical_angle, depth, mach |
| `event:/aircraft/engines/engine05_r15B300_WEP_ai` | headphones, Distance, Event Cone Angle, Elevation, load, Direction, is_enemy, rpm, is_visible, mach, speed_relative, depth |
| `event:/aircraft/engines/engine05_r15B300_WEP_cockpit_l` | zoom, overload, cockpit_open, Distance, load, wep, rpm, depth |
| `event:/aircraft/engines/engine05_r15B300_WEP_cockpit_r` | cockpit_open, Distance, load, wep, rpm, overload, zoom |
| `event:/aircraft/engines/engine05_r15B300_start` | Distance |
| `event:/aircraft/engines/engine05_r15B300_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_r15B300_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_r15B300_stop` | Distance |
| `event:/aircraft/engines/engine05_r15B300_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_r15B300_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_r195` | load, rpm, wep, Event Cone Angle, zoom, overload, speed, mach, event_vertical_angle, depth, Distance |
| `event:/aircraft/engines/engine05_r195_ai` | mach, depth, speed_relative, is_visible, rpm, is_enemy, Direction, load, Distance, Elevation, Event Cone Angle, headphones |
| `event:/aircraft/engines/engine05_r195_cockpit_l` | zoom, overload, wep, rpm, cockpit_open, Distance, load, depth |
| `event:/aircraft/engines/engine05_r195_cockpit_r` | Distance, cockpit_open, load, rpm, wep, overload, zoom |
| `event:/aircraft/engines/engine05_r195_start` | Distance |
| `event:/aircraft/engines/engine05_r195_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_r195_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_r195_stop` | Distance |
| `event:/aircraft/engines/engine05_r195_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_r195_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_r28_N1` | depth, event_vertical_angle, mach, Distance, load, Event Cone Angle, wep, rpm, zoom, overload, speed |
| `event:/aircraft/engines/engine05_r28_N1_ai` | Direction, is_enemy, rpm, is_visible, mach, depth, speed_relative, headphones, Distance, Elevation, Event Cone Angle, load |
| `event:/aircraft/engines/engine05_r28_N1_cockpit_l` | rpm, wep, Distance, cockpit_open, load, overload, zoom, depth |
| `event:/aircraft/engines/engine05_r28_N1_cockpit_r` | Distance, cockpit_open, load, rpm, wep, overload, zoom |
| `event:/aircraft/engines/engine05_r28_N1_start` | Distance |
| `event:/aircraft/engines/engine05_r28_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_r28_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_r28_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_r28_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_r28_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_r79b300_WEP` | speed, zoom, overload, wep, Event Cone Angle, load, Distance, rpm, mach, event_vertical_angle, depth |
| `event:/aircraft/engines/engine05_r79b300_WEP_ai` | rpm, is_enemy, Direction, mach, depth, speed_relative, is_visible, headphones, load, Distance, Elevation, Event Cone Angle |
| `event:/aircraft/engines/engine05_r79b300_WEP_cockpit_l` | wep, load, cockpit_open, Distance, overload, zoom, rpm, depth |
| `event:/aircraft/engines/engine05_r79b300_WEP_cockpit_r` | overload, zoom, wep, Distance, cockpit_open, load, rpm |
| `event:/aircraft/engines/engine05_r79b300_start` | Distance |
| `event:/aircraft/engines/engine05_r79b300_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_r79b300_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_r79b300_stop` | Distance |
| `event:/aircraft/engines/engine05_r79b300_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_r79b300_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_rM8A_N1` | Distance, depth, event_vertical_angle, rpm, mach, speed, overload, zoom, Event Cone Angle, wep, load |
| `event:/aircraft/engines/engine05_rM8A_N1_ai` | is_visible, mach, depth, speed_relative, Direction, is_enemy, rpm, Distance, Elevation, Event Cone Angle, load, headphones |
| `event:/aircraft/engines/engine05_rM8A_N1_cockpit_l` | overload, zoom, wep, Distance, cockpit_open, load, depth, rpm |
| `event:/aircraft/engines/engine05_rM8A_N1_cockpit_r` | rpm, overload, zoom, Distance, cockpit_open, load, wep |
| `event:/aircraft/engines/engine05_rM8A_N1_start` | Distance |
| `event:/aircraft/engines/engine05_rM8A_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_rM8A_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_rM8A_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_rM8A_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_rM8A_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_rb199_WEP` | zoom, overload, speed, load, Event Cone Angle, wep, depth, event_vertical_angle, rpm, mach, Distance |
| `event:/aircraft/engines/engine05_rb199_WEP_ai` | load, Distance, Event Cone Angle, Elevation, headphones, mach, speed_relative, depth, is_visible, rpm, is_enemy, Direction |
| `event:/aircraft/engines/engine05_rb199_WEP_cockpit_l` | cockpit_open, Distance, load, wep, zoom, overload, depth, rpm |
| `event:/aircraft/engines/engine05_rb199_WEP_cockpit_r` | rpm, wep, load, cockpit_open, Distance, overload, zoom |
| `event:/aircraft/engines/engine05_rb199_start` | Distance |
| `event:/aircraft/engines/engine05_rb199_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_rb199_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_rb199_stop` | Distance |
| `event:/aircraft/engines/engine05_rb199_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_rb199_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_rb_168_sprey_WEP` | speed, zoom, overload, Event Cone Angle, load, Distance, depth, event_vertical_angle, mach, rpm |
| `event:/aircraft/engines/engine05_rb_168_sprey_WEP_ai` | rpm, is_enemy, Direction, mach, speed_relative, depth, is_visible, headphones, load, Distance, Event Cone Angle, Elevation |
| `event:/aircraft/engines/engine05_rb_168_sprey_WEP_cockpit_l` | depth, rpm, Distance, cockpit_open, load, wep, zoom, overload |
| `event:/aircraft/engines/engine05_rb_168_sprey_WEP_cockpit_r` | overload, zoom, cockpit_open, Distance, load, wep, rpm |
| `event:/aircraft/engines/engine05_rb_168_sprey_start` | Distance |
| `event:/aircraft/engines/engine05_rb_168_sprey_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_rb_168_sprey_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_rb_168_sprey_stop` | Distance |
| `event:/aircraft/engines/engine05_rb_168_sprey_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_rb_168_sprey_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_rd33_WEP` | Distance, rpm, mach, depth, event_vertical_angle, speed, zoom, overload, wep, Event Cone Angle, load |
| `event:/aircraft/engines/engine05_rd33_WEP_ai` | Direction, rpm, is_enemy, is_visible, depth, speed_relative, mach, headphones, Elevation, Event Cone Angle, Distance, load |
| `event:/aircraft/engines/engine05_rd33_WEP_cockpit_l` | load, Distance, cockpit_open, wep, overload, zoom, rpm, depth |
| `event:/aircraft/engines/engine05_rd33_WEP_cockpit_r` | zoom, overload, wep, load, Distance, cockpit_open, rpm |
| `event:/aircraft/engines/engine05_rd33_start` | Distance |
| `event:/aircraft/engines/engine05_rd33_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_rd33_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_rd33_stop` | Distance |
| `event:/aircraft/engines/engine05_rd33_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_rd33_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_rd9_N1` | wep, rpm, Event Cone Angle, load, speed, zoom, overload, Distance, mach, event_vertical_angle, depth |
| `event:/aircraft/engines/engine05_rd9_N1_WEP` | mach, depth, event_vertical_angle, Distance, overload, zoom, speed, load, rpm, wep, Event Cone Angle |
| `event:/aircraft/engines/engine05_rd9_N1_WEP_ai` | is_visible, mach, depth, speed_relative, Direction, rpm, is_enemy, Distance, Elevation, Event Cone Angle, load, headphones |
| `event:/aircraft/engines/engine05_rd9_N1_WEP_cockpit_l` | depth, zoom, overload, Distance, cockpit_open, load, rpm, wep |
| `event:/aircraft/engines/engine05_rd9_N1_WEP_cockpit_r` | cockpit_open, Distance, load, wep, rpm, zoom, overload |
| `event:/aircraft/engines/engine05_rd9_N1_ai` | headphones, load, Elevation, Event Cone Angle, Distance, rpm, is_enemy, Direction, depth, speed_relative, mach, is_visible |
| `event:/aircraft/engines/engine05_rd9_N1_cockpit_l` | depth, rpm, wep, Distance, cockpit_open, load, overload, zoom |
| `event:/aircraft/engines/engine05_rd9_N1_cockpit_r` | overload, zoom, load, cockpit_open, Distance, wep, rpm |
| `event:/aircraft/engines/engine05_rd9_N1_start` | Distance |
| `event:/aircraft/engines/engine05_rd9_N1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_rd9_N1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_rd9_N1_stop` | Distance |
| `event:/aircraft/engines/engine05_rd9_N1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_rd9_N1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine05_snecma_turbomecha` | depth, event_vertical_angle, mach, Distance, overload, zoom, speed, load, Event Cone Angle, rpm, wep |
| `event:/aircraft/engines/engine05_snecma_turbomecha_ai` | rpm, is_enemy, Direction, speed_relative, depth, mach, is_visible, headphones, load, Event Cone Angle, Elevation, Distance |
| `event:/aircraft/engines/engine05_snecma_turbomecha_cockpit_l` | depth, zoom, overload, cockpit_open, Distance, load, wep, rpm |
| `event:/aircraft/engines/engine05_snecma_turbomecha_cockpit_r` | Distance, cockpit_open, load, rpm, wep, zoom, overload |
| `event:/aircraft/engines/engine05_snecma_turbomecha_start` | Distance |
| `event:/aircraft/engines/engine05_snecma_turbomecha_start_cockpit_l` |  |
| `event:/aircraft/engines/engine05_snecma_turbomecha_start_cockpit_r` |  |
| `event:/aircraft/engines/engine05_snecma_turbomecha_stop` | Distance |
| `event:/aircraft/engines/engine05_snecma_turbomecha_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine05_snecma_turbomecha_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine06` | load, Event Cone Angle, rpm, overload, zoom, depth, event_vertical_angle, Distance |
| `event:/aircraft/engines/engine06_ai` | load, Elevation, Event Cone Angle, rpm, Distance, headphones, listener_is_ground, speed_relative, is_visible, is_enemy, Direction |
| `event:/aircraft/engines/engine06_cockpit_l` | Distance, depth, rpm, load, cockpit_open, zoom, overload |
| `event:/aircraft/engines/engine06_cockpit_r` | Distance, overload, zoom, load, cockpit_open, rpm |
| `event:/aircraft/engines/engine06_prop` | Distance |
| `event:/aircraft/engines/engine06_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine06_prop_cockpit_r` | loop, Distance |
| `event:/aircraft/engines/engine06_start` | Distance |
| `event:/aircraft/engines/engine06_start_cockpit_l` |  |
| `event:/aircraft/engines/engine06_start_cockpit_r` |  |
| `event:/aircraft/engines/engine06_stop` | Distance |
| `event:/aircraft/engines/engine06_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine06_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine07` | Distance, depth, event_vertical_angle, zoom, overload, Event Cone Angle, rpm, load |
| `event:/aircraft/engines/engine07_ai` | is_enemy, Direction, speed_relative, listener_is_ground, is_visible, headphones, load, rpm, Distance, Event Cone Angle, Elevation |
| `event:/aircraft/engines/engine07_cockpit_l` | zoom, overload, rpm, cockpit_open, load, Distance, depth |
| `event:/aircraft/engines/engine07_cockpit_r` | overload, zoom, rpm, load, cockpit_open, Distance |
| `event:/aircraft/engines/engine07_corsair` | SpeedAbs, overload, zoom, rpm, Event Cone Angle, load, Distance, event_vertical_angle, depth |
| `event:/aircraft/engines/engine07_corsair_ai` | load, Distance, rpm, Event Cone Angle, Elevation, headphones, speed_relative, listener_is_ground, is_visible, is_enemy, Direction |
| `event:/aircraft/engines/engine07_prop` | Distance |
| `event:/aircraft/engines/engine07_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine07_prop_cockpit_r` | loop, Distance |
| `event:/aircraft/engines/engine07_start` | Distance |
| `event:/aircraft/engines/engine07_start_cockpit_l` |  |
| `event:/aircraft/engines/engine07_start_cockpit_r` |  |
| `event:/aircraft/engines/engine07_stop` | Distance |
| `event:/aircraft/engines/engine07_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine07_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine08` | depth, event_vertical_angle, Distance, overload, zoom, SpeedAbs, load, rpm, Event Cone Angle |
| `event:/aircraft/engines/engine08_ai` | load, Event Cone Angle, Elevation, Distance, rpm, headphones, speed_relative, listener_is_ground, is_visible, is_enemy, Direction |
| `event:/aircraft/engines/engine08_cockpit_l` | depth, Distance, load, cockpit_open, rpm, zoom, overload |
| `event:/aircraft/engines/engine08_cockpit_r` | load, cockpit_open, rpm, overload, zoom, Distance |
| `event:/aircraft/engines/engine08_prop` | Distance |
| `event:/aircraft/engines/engine08_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine08_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine08_start` | Distance |
| `event:/aircraft/engines/engine08_start_cockpit_l` | Distance |
| `event:/aircraft/engines/engine08_start_cockpit_r` | Distance |
| `event:/aircraft/engines/engine08_stop` | Distance |
| `event:/aircraft/engines/engine08_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine08_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine09` | overload, zoom, rpm, Event Cone Angle, load, Distance, event_vertical_angle, depth |
| `event:/aircraft/engines/engine09_ai` | speed_relative, listener_is_ground, is_visible, is_enemy, Direction, load, Distance, rpm, Event Cone Angle, Elevation, headphones |
| `event:/aircraft/engines/engine09_cockpit_l` | Distance, depth, rpm, cockpit_open, load, overload, zoom |
| `event:/aircraft/engines/engine09_cockpit_r` | load, cockpit_open, rpm, zoom, overload, Distance |
| `event:/aircraft/engines/engine09_prop` | Distance |
| `event:/aircraft/engines/engine09_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine09_prop_cockpit_r` | loop, Distance |
| `event:/aircraft/engines/engine09_start` | Event Cone Angle, load, Distance |
| `event:/aircraft/engines/engine09_start_cockpit_l` | load |
| `event:/aircraft/engines/engine09_start_cockpit_r` | load |
| `event:/aircraft/engines/engine09_stop` | Distance |
| `event:/aircraft/engines/engine09_stop_cockpit_l` | Distance |
| `event:/aircraft/engines/engine09_stop_cockpit_r` | Distance |
| `event:/aircraft/engines/engine10` | event_vertical_angle, depth, Distance, overload, zoom, load, rpm, Event Cone Angle |
| `event:/aircraft/engines/engine10_ai` | is_visible, speed_relative, listener_is_ground, Direction, is_enemy, rpm, Distance, Event Cone Angle, Elevation, load, headphones |
| `event:/aircraft/engines/engine10_cockpit_l` | cockpit_open, load, rpm, zoom, overload, depth, Distance |
| `event:/aircraft/engines/engine10_cockpit_r` | Distance, rpm, load, cockpit_open, zoom, overload |
| `event:/aircraft/engines/engine10_prop` | Distance |
| `event:/aircraft/engines/engine10_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine10_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine10_start` | load, Event Cone Angle, Distance |
| `event:/aircraft/engines/engine10_start_cockpit_l` | load |
| `event:/aircraft/engines/engine10_start_cockpit_r` | load |
| `event:/aircraft/engines/engine10_stop` | Distance |
| `event:/aircraft/engines/engine10_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine10_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine11` | Event Cone Angle, rpm, load, overload, zoom, Distance, event_vertical_angle, depth |
| `event:/aircraft/engines/engine11_ai` | load, Distance, rpm, Event Cone Angle, Elevation, headphones, speed_relative, listener_is_ground, is_visible, is_enemy, Direction |
| `event:/aircraft/engines/engine11_cockpit_l` | depth, Distance, overload, zoom, cockpit_open, load, rpm |
| `event:/aircraft/engines/engine11_cockpit_r` | zoom, overload, rpm, load, cockpit_open, Distance |
| `event:/aircraft/engines/engine11_prop` | Distance |
| `event:/aircraft/engines/engine11_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine11_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine11_start` | load, Event Cone Angle, Distance |
| `event:/aircraft/engines/engine11_start_cockpit_l` | load |
| `event:/aircraft/engines/engine11_start_cockpit_r` | load |
| `event:/aircraft/engines/engine11_stop` | Distance |
| `event:/aircraft/engines/engine11_stop_cockpit_l` | Distance |
| `event:/aircraft/engines/engine11_stop_cockpit_r` | Distance |
| `event:/aircraft/engines/engine12` | rpm, Event Cone Angle, load, overload, zoom, Distance, depth, event_vertical_angle |
| `event:/aircraft/engines/engine12_ai` | speed_relative, listener_is_ground, is_visible, is_enemy, Direction, load, Distance, rpm, Event Cone Angle, Elevation, headphones |
| `event:/aircraft/engines/engine12_cockpit_l` | zoom, overload, rpm, cockpit_open, load, Distance, depth |
| `event:/aircraft/engines/engine12_cockpit_r` | rpm, load, cockpit_open, overload, zoom, Distance |
| `event:/aircraft/engines/engine12_prop` | Distance |
| `event:/aircraft/engines/engine12_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine12_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine12_start` | Event Cone Angle, load, Distance |
| `event:/aircraft/engines/engine12_start_cockpit_l` | load |
| `event:/aircraft/engines/engine12_start_cockpit_r` | load |
| `event:/aircraft/engines/engine12_stop` | Distance |
| `event:/aircraft/engines/engine12_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine12_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine13` | load, rpm, Event Cone Angle, overload, zoom, event_vertical_angle, depth, Distance |
| `event:/aircraft/engines/engine13_ai` | Elevation, Event Cone Angle, rpm, Distance, load, headphones, is_visible, listener_is_ground, speed_relative, Direction, is_enemy |
| `event:/aircraft/engines/engine13_cockpit_l` | zoom, overload, load, cockpit_open, rpm, depth, Distance |
| `event:/aircraft/engines/engine13_cockpit_r` | Distance, rpm, cockpit_open, load, zoom, overload |
| `event:/aircraft/engines/engine13_prop` | Distance |
| `event:/aircraft/engines/engine13_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine13_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine13_start` | Distance |
| `event:/aircraft/engines/engine13_start_cockpit_l` |  |
| `event:/aircraft/engines/engine13_start_cockpit_r` |  |
| `event:/aircraft/engines/engine13_stop` | Distance |
| `event:/aircraft/engines/engine13_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine13_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine14` | depth, event_vertical_angle, Distance, zoom, overload, load, Event Cone Angle, rpm |
| `event:/aircraft/engines/engine14_ai` | Elevation, Event Cone Angle, Distance, rpm, load, headphones, is_visible, listener_is_ground, speed_relative, Direction, is_enemy |
| `event:/aircraft/engines/engine14_cockpit_l` | depth, Distance, load, cockpit_open, rpm, overload, zoom |
| `event:/aircraft/engines/engine14_cockpit_r` | zoom, overload, rpm, load, cockpit_open, Distance |
| `event:/aircraft/engines/engine14_prop` | Distance |
| `event:/aircraft/engines/engine14_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine14_prop_cockpit_r` | loop, Distance |
| `event:/aircraft/engines/engine14_start` | Distance |
| `event:/aircraft/engines/engine14_start_cockpit_l` | Distance |
| `event:/aircraft/engines/engine14_start_cockpit_r` | Distance |
| `event:/aircraft/engines/engine14_stop` | Distance |
| `event:/aircraft/engines/engine14_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine14_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine15` | depth, event_vertical_angle, Distance, zoom, overload, load, Event Cone Angle, rpm |
| `event:/aircraft/engines/engine15_ai` | Event Cone Angle, Elevation, Distance, rpm, load, headphones, is_visible, speed_relative, listener_is_ground, Direction, is_enemy |
| `event:/aircraft/engines/engine15_cockpit_l` | cockpit_open, load, Elevation, rpm, headphones, zoom, overload, depth, Distance, Direction |
| `event:/aircraft/engines/engine15_cockpit_r` | load, cockpit_open, rpm, Elevation, overload, zoom, headphones, Distance, Direction |
| `event:/aircraft/engines/engine15_prop` | Distance |
| `event:/aircraft/engines/engine15_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine15_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine15_start` | Distance, load, Event Cone Angle |
| `event:/aircraft/engines/engine15_start_cockpit_l` | load |
| `event:/aircraft/engines/engine15_start_cockpit_r` | load |
| `event:/aircraft/engines/engine15_stop` | Distance |
| `event:/aircraft/engines/engine15_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine15_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine16` | zoom, overload, Event Cone Angle, rpm, load, Distance, event_vertical_angle, depth |
| `event:/aircraft/engines/engine16_ai` | Distance, rpm, Event Cone Angle, Elevation, load, headphones, is_visible, speed_relative, listener_is_ground, Direction, is_enemy |
| `event:/aircraft/engines/engine16_cockpit_l` | overload, zoom, rpm, load, cockpit_open, Distance, depth |
| `event:/aircraft/engines/engine16_cockpit_r` | zoom, overload, load, cockpit_open, rpm, Distance |
| `event:/aircraft/engines/engine16_prop` | Distance |
| `event:/aircraft/engines/engine16_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine16_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine16_start` | Distance |
| `event:/aircraft/engines/engine16_start_cockpit_l` |  |
| `event:/aircraft/engines/engine16_start_cockpit_r` |  |
| `event:/aircraft/engines/engine16_stop` | Distance |
| `event:/aircraft/engines/engine16_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine16_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine17` | Distance, event_vertical_angle, depth, overload, zoom, Event Cone Angle, rpm, load |
| `event:/aircraft/engines/engine17_ai` | headphones, load, Distance, rpm, Elevation, Event Cone Angle, is_enemy, Direction, listener_is_ground, speed_relative, is_visible |
| `event:/aircraft/engines/engine17_cockpit_l` | Distance, depth, overload, zoom, rpm, load, cockpit_open |
| `event:/aircraft/engines/engine17_cockpit_r` | Distance, rpm, load, cockpit_open, overload, zoom |
| `event:/aircraft/engines/engine17_mk2` | event_vertical_angle, depth, Distance, load, rpm, Event Cone Angle, overload, zoom |
| `event:/aircraft/engines/engine17_mk2_ai` | Direction, is_enemy, is_visible, listener_is_ground, speed_relative, headphones, rpm, Distance, Elevation, Event Cone Angle, load |
| `event:/aircraft/engines/engine17_mk2_cockpit_l` | Distance, depth, rpm, Event Cone Angle, load, cockpit_open, overload, zoom |
| `event:/aircraft/engines/engine17_mk2_cockpit_r` | Distance, zoom, overload, rpm, Event Cone Angle, load, cockpit_open |
| `event:/aircraft/engines/engine17_mk2_prop` | Distance |
| `event:/aircraft/engines/engine17_mk2_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine17_mk2_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine17_mk2_start` | Event Cone Angle, load, Distance |
| `event:/aircraft/engines/engine17_mk2_start_cockpit_l` | load |
| `event:/aircraft/engines/engine17_mk2_start_cockpit_r` | load |
| `event:/aircraft/engines/engine17_mk2_stop` | Distance |
| `event:/aircraft/engines/engine17_mk2_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine17_mk2_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine17_prop` | Distance |
| `event:/aircraft/engines/engine17_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine17_prop_cockpit_r` | loop, Distance |
| `event:/aircraft/engines/engine17_start` | load, Event Cone Angle, Distance |
| `event:/aircraft/engines/engine17_start_cockpit_l` | load |
| `event:/aircraft/engines/engine17_start_cockpit_r` | load |
| `event:/aircraft/engines/engine17_stop` | Distance |
| `event:/aircraft/engines/engine17_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine17_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine18` | Event Cone Angle, rpm, load, overload, zoom, Distance, event_vertical_angle, depth |
| `event:/aircraft/engines/engine18_ai` | Direction, is_enemy, is_visible, listener_is_ground, speed_relative, headphones, rpm, Distance, Elevation, Event Cone Angle, load |
| `event:/aircraft/engines/engine18_cockpit_l` | load, cockpit_open, rpm, zoom, overload, depth, Distance |
| `event:/aircraft/engines/engine18_cockpit_r` | Distance, rpm, load, cockpit_open, overload, zoom |
| `event:/aircraft/engines/engine18_prop` | Distance |
| `event:/aircraft/engines/engine18_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine18_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine18_start` | Event Cone Angle, load, Distance |
| `event:/aircraft/engines/engine18_start_cockpit_l` | load |
| `event:/aircraft/engines/engine18_start_cockpit_r` | load |
| `event:/aircraft/engines/engine18_stop` | Distance |
| `event:/aircraft/engines/engine18_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine18_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine19` | load, rpm, Event Cone Angle, overload, zoom, event_vertical_angle, depth, Distance |
| `event:/aircraft/engines/engine19_ai` | load, rpm, Distance, Elevation, Event Cone Angle, headphones, listener_is_ground, speed_relative, is_visible, is_enemy, Direction |
| `event:/aircraft/engines/engine19_cockpit_l` | cockpit_open, load, rpm, overload, zoom, depth, Distance |
| `event:/aircraft/engines/engine19_cockpit_r` | Distance, rpm, cockpit_open, load, overload, zoom |
| `event:/aircraft/engines/engine19_prop` | Distance |
| `event:/aircraft/engines/engine19_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine19_prop_cockpit_r` | loop, Distance |
| `event:/aircraft/engines/engine19_start` | Event Cone Angle, load, Distance |
| `event:/aircraft/engines/engine19_start_cockpit_l` | load |
| `event:/aircraft/engines/engine19_start_cockpit_r` | load |
| `event:/aircraft/engines/engine19_stop` | Distance |
| `event:/aircraft/engines/engine19_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine19_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine20` | event_vertical_angle, depth, Distance, rpm2, broken, load, rpm, Event Cone Angle, zoom, overload |
| `event:/aircraft/engines/engine20_ai` | load, rpm, Distance, Elevation, Event Cone Angle, headphones, listener_is_ground, speed_relative, is_visible, rpm2, is_enemy, Direction |
| `event:/aircraft/engines/engine20_cockpit_l` | load, cockpit_open, zoom, overload, Distance, depth, rpm2, broken |
| `event:/aircraft/engines/engine20_cockpit_r` | cockpit_open, load, zoom, overload, Distance, broken, rpm2 |
| `event:/aircraft/engines/engine20_prop` | Distance |
| `event:/aircraft/engines/engine20_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine20_prop_cockpit_r` | loop, Distance |
| `event:/aircraft/engines/engine20_start` | load, Event Cone Angle, Distance |
| `event:/aircraft/engines/engine20_start_cockpit_l` | load |
| `event:/aircraft/engines/engine20_start_cockpit_r` | load |
| `event:/aircraft/engines/engine20_stop` | zoom, Event Cone Angle, load, broken, rpm2, Distance |
| `event:/aircraft/engines/engine20_stop_cockpit_l` | zoom, cockpit_open, rpm2, Distance |
| `event:/aircraft/engines/engine20_stop_cockpit_r` | rpm2, Distance, zoom, cockpit_open |
| `event:/aircraft/engines/engine21` | event_vertical_angle, depth, Distance, load, Event Cone Angle, rpm, overload, zoom |
| `event:/aircraft/engines/engine21_ai` | is_visible, listener_is_ground, speed_relative, Direction, is_enemy, rpm, Distance, Elevation, Event Cone Angle, load, headphones |
| `event:/aircraft/engines/engine21_cockpit_l` | depth, Distance, zoom, overload, cockpit_open, load, rpm |
| `event:/aircraft/engines/engine21_cockpit_r` | zoom, overload, rpm, load, cockpit_open, Distance |
| `event:/aircraft/engines/engine21_prop` | Distance |
| `event:/aircraft/engines/engine21_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine21_prop_cockpit_r` | loop, Distance |
| `event:/aircraft/engines/engine21_start` | Distance |
| `event:/aircraft/engines/engine21_start_cockpit_l` |  |
| `event:/aircraft/engines/engine21_start_cockpit_r` |  |
| `event:/aircraft/engines/engine21_stop` | Distance |
| `event:/aircraft/engines/engine21_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine21_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine22` | Event Cone Angle, rpm, load, zoom, overload, Distance, depth, event_vertical_angle |
| `event:/aircraft/engines/engine22_ai` | headphones, load, Event Cone Angle, Elevation, rpm, Distance, is_enemy, Direction, speed_relative, listener_is_ground, is_visible |
| `event:/aircraft/engines/engine22_cockpit_l` | Distance, depth, zoom, overload, rpm, load, cockpit_open |
| `event:/aircraft/engines/engine22_cockpit_r` | Distance, zoom, overload, rpm, load, cockpit_open |
| `event:/aircraft/engines/engine22_prop` | Distance |
| `event:/aircraft/engines/engine22_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine22_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine22_start` | Distance |
| `event:/aircraft/engines/engine22_start_cockpit_l` |  |
| `event:/aircraft/engines/engine22_start_cockpit_r` |  |
| `event:/aircraft/engines/engine22_stop` | Distance |
| `event:/aircraft/engines/engine22_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine22_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine24` | speed, overload, zoom, Event Cone Angle, wep, rpm, volume_ducking, load, Distance, depth |
| `event:/aircraft/engines/engine24_ai` | Direction, rpm, is_enemy, is_visible, mach, listener_is_ground, depth, speed_relative, headphones, Distance, Elevation, Event Cone Angle, load |
| `event:/aircraft/engines/engine24_cockpit_l` | depth, zoom, overload, wep, rpm, cockpit_open, Distance, volume_ducking, load |
| `event:/aircraft/engines/engine24_cockpit_r` | zoom, overload, cockpit_open, Distance, volume_ducking, load, wep, rpm |
| `event:/aircraft/engines/engine24_start` | Distance |
| `event:/aircraft/engines/engine24_start_cockpit_l` |  |
| `event:/aircraft/engines/engine24_start_cockpit_r` |  |
| `event:/aircraft/engines/engine24_stop` | Distance |
| `event:/aircraft/engines/engine24_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine24_stop_cockpit_r` |  |
| `event:/aircraft/engines/engineBooster` | speed, overload, zoom, rpm, Event Cone Angle, load, volume_ducking, Distance, depth |
| `event:/aircraft/engines/engineBooster_ai` | is_visible, listener_is_ground, depth, speed_relative, mach, Direction, is_enemy, Elevation, Event Cone Angle, rpm, Distance, load, headphones |
| `event:/aircraft/engines/engineBooster_cockpit` | cockpit_open, Distance, volume_ducking, load, wep, rpm, zoom, overload, depth |
| `event:/aircraft/engines/engine_ah56_prop_cockpit_l` | rpm, cockpit_open, load, rotor_broken, Distance |
| `event:/aircraft/engines/engine_ah56_prop_cockpit_r` | Distance, rotor_broken, load, cockpit_open, rpm |
| `event:/aircraft/engines/engine_ah56_prop_l` | Event Cone Angle, rpm, Distance, rotor_broken |
| `event:/aircraft/engines/engine_ah56_prop_r` | Distance, rotor_broken, Event Cone Angle, rpm |
| `event:/aircraft/engines/engine_ah64_cockpit_l` | depth, Distance, broken, rpm2, rotor_broken, cockpit_open, load, overload, zoom |
| `event:/aircraft/engines/engine_ah64_cockpit_r` | rpm2, broken, rotor_broken, Distance, zoom, overload, load, cockpit_open |
| `event:/aircraft/engines/engine_ah64_l` | zoom, load, Event Cone Angle, broken, rpm2, rotor_broken, depth, Distance |
| `event:/aircraft/engines/engine_ah64_prop_cockpit_l` | Distance, rotor_broken, load, cockpit_open, rpm |
| `event:/aircraft/engines/engine_ah64_prop_cockpit_r` | cockpit_open, load, rpm, Distance, rotor_broken |
| `event:/aircraft/engines/engine_ah64_prop_l` | rpm, Event Cone Angle, rotor_broken, Distance |
| `event:/aircraft/engines/engine_ah64_prop_r` | Distance, rotor_broken, Event Cone Angle, rpm |
| `event:/aircraft/engines/engine_ah64_r` | Distance, broken, rpm2, rotor_broken, load, Event Cone Angle, zoom |
| `event:/aircraft/engines/engine_ah64_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_ah64_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_ah64_start_l` | Distance |
| `event:/aircraft/engines/engine_ah64_start_r` | Distance |
| `event:/aircraft/engines/engine_ah64_stop_cockpit_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_ah64_stop_cockpit_r` | rpm2, Distance |
| `event:/aircraft/engines/engine_ah64_stop_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_ah64_stop_r` | Distance, rpm2 |
| `event:/aircraft/engines/engine_ai_start` | Distance |
| `event:/aircraft/engines/engine_ai_stop` | Distance |
| `event:/aircraft/engines/engine_bo_105_cockpit_l` | Distance, depth, rotor_broken, rpm2, broken, load, cockpit_open, zoom, overload |
| `event:/aircraft/engines/engine_bo_105_cockpit_r` | rpm2, broken, rotor_broken, Distance, overload, zoom, load, cockpit_open |
| `event:/aircraft/engines/engine_bo_105_l` | Distance, depth, rotor_broken, broken, rpm2, Event Cone Angle, load, zoom |
| `event:/aircraft/engines/engine_bo_105_prop_cockpit_l` | cockpit_open, load, rpm, rotor_broken, broken |
| `event:/aircraft/engines/engine_bo_105_prop_cockpit_r` | rpm, load, cockpit_open, broken, rotor_broken |
| `event:/aircraft/engines/engine_bo_105_prop_l` | rpm, Event Cone Angle, load, rotor_broken, broken, Distance, depth |
| `event:/aircraft/engines/engine_bo_105_prop_r` | rpm, load, Event Cone Angle, broken, rotor_broken, Distance |
| `event:/aircraft/engines/engine_bo_105_r` | load, Event Cone Angle, zoom, Distance, rpm2, broken, rotor_broken |
| `event:/aircraft/engines/engine_bo_105_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_bo_105_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_bo_105_start_l` | Distance |
| `event:/aircraft/engines/engine_bo_105_start_r` | Distance |
| `event:/aircraft/engines/engine_bo_105_stop_cockpit_l` | rpm2, Distance |
| `event:/aircraft/engines/engine_bo_105_stop_cockpit_r` | Distance, rpm2 |
| `event:/aircraft/engines/engine_bo_105_stop_l` | rpm2, Distance |
| `event:/aircraft/engines/engine_bo_105_stop_r` | Distance, rpm2 |
| `event:/aircraft/engines/engine_bomber_ai_start` | Distance |
| `event:/aircraft/engines/engine_bomber_ai_stop` | Distance |
| `event:/aircraft/engines/engine_bv138` | event_vertical_angle, depth, Distance, overload, zoom, load, Event Cone Angle, rpm |
| `event:/aircraft/engines/engine_bv138_ai` | is_visible, listener_is_ground, speed_relative, Direction, is_enemy, Elevation, Event Cone Angle, rpm, Distance, load, headphones |
| `event:/aircraft/engines/engine_bv138_cockpit_l` | overload, zoom, cockpit_open, load, Event Cone Angle, rpm, depth, Distance |
| `event:/aircraft/engines/engine_bv138_cockpit_r` | Distance, cockpit_open, load, Event Cone Angle, rpm, zoom, overload |
| `event:/aircraft/engines/engine_bv138_prop` | Distance |
| `event:/aircraft/engines/engine_bv138_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine_bv138_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine_bv138_start` | Distance |
| `event:/aircraft/engines/engine_bv138_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_bv138_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_bv138_stop` | Distance |
| `event:/aircraft/engines/engine_bv138_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine_bv138_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine_dive` | Distance, dive |
| `event:/aircraft/engines/engine_do335` | Event Cone Angle, rpm, load, zoom, overload, Distance, depth, event_vertical_angle |
| `event:/aircraft/engines/engine_do335_ai` | load, Elevation, Event Cone Angle, Distance, rpm, headphones, listener_is_ground, speed_relative, is_visible, is_enemy, Direction |
| `event:/aircraft/engines/engine_do335_cockpit_l` | Distance, depth, overload, zoom, Event Cone Angle, rpm, cockpit_open, load |
| `event:/aircraft/engines/engine_do335_cockpit_r` | rpm, Event Cone Angle, load, cockpit_open, zoom, overload, Distance |
| `event:/aircraft/engines/engine_do335_prop` | Distance |
| `event:/aircraft/engines/engine_do335_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine_do335_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine_do335_start` | load, Event Cone Angle, Distance |
| `event:/aircraft/engines/engine_do335_start_cockpit_l` | load |
| `event:/aircraft/engines/engine_do335_start_cockpit_r` | load |
| `event:/aircraft/engines/engine_do335_stop` | Distance |
| `event:/aircraft/engines/engine_do335_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine_do335_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine_heli_ai` | is_enemy, Direction, rpm2, is_visible, headphones, Distance, load, Elevation, Event Cone Angle |
| `event:/aircraft/engines/engine_heli_ai_start` | is_enemy, Direction, is_visible, headphones, Distance, Elevation |
| `event:/aircraft/engines/engine_heli_ai_stop` | Direction, is_enemy, is_visible, rpm2, Distance, headphones, Elevation |
| `event:/aircraft/engines/engine_heli_small_ai` | is_enemy, Direction, rpm2, is_visible, headphones, Distance, load, Elevation, Event Cone Angle |
| `event:/aircraft/engines/engine_hp_12` | rpm, Event Cone Angle, load, zoom, overload, Distance, depth, event_vertical_angle |
| `event:/aircraft/engines/engine_hp_12_ai` | speed_relative, listener_is_ground, is_visible, is_enemy, Direction, load, Event Cone Angle, Elevation, rpm, Distance, headphones |
| `event:/aircraft/engines/engine_hp_12_cockpit_l` | zoom, overload, cockpit_open, load, rpm, depth, Distance |
| `event:/aircraft/engines/engine_hp_12_cockpit_r` | rpm, load, cockpit_open, zoom, overload, Distance |
| `event:/aircraft/engines/engine_hp_12_prop` | Distance |
| `event:/aircraft/engines/engine_hp_12_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine_hp_12_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine_hp_12_start` | Distance |
| `event:/aircraft/engines/engine_hp_12_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_hp_12_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_hp_12_stop` | Distance |
| `event:/aircraft/engines/engine_hp_12_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine_hp_12_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine_j7w1` | zoom, overload, rpm, Event Cone Angle, load, Distance, depth, event_vertical_angle |
| `event:/aircraft/engines/engine_j7w1_ai` | headphones, Distance, rpm, Event Cone Angle, Elevation, load, Direction, is_enemy, is_visible, speed_relative, listener_is_ground |
| `event:/aircraft/engines/engine_j7w1_cockpit_l` | zoom, overload, rpm, load, cockpit_open, Distance, depth |
| `event:/aircraft/engines/engine_j7w1_cockpit_r` | rpm, load, cockpit_open, zoom, overload, Distance |
| `event:/aircraft/engines/engine_j7w1_prop` | Distance |
| `event:/aircraft/engines/engine_j7w1_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine_j7w1_prop_cockpit_r` | loop, Distance |
| `event:/aircraft/engines/engine_j7w1_start` | Distance |
| `event:/aircraft/engines/engine_j7w1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_j7w1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_j7w1_stop` | Distance |
| `event:/aircraft/engines/engine_j7w1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine_j7w1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine_jet_ai_start` | Distance |
| `event:/aircraft/engines/engine_jet_ai_stop` | Distance |
| `event:/aircraft/engines/engine_jet_far_ai` | Event Cone Angle, Distance, load, listener_is_ground, Direction, rpm |
| `event:/aircraft/engines/engine_jet_hunter_far_ai` | listener_is_ground, Direction, rpm, Event Cone Angle, Distance, load |
| `event:/aircraft/engines/engine_jet_meteor_far_ai` | rpm, Direction, listener_is_ground, load, Event Cone Angle, Distance |
| `event:/aircraft/engines/engine_ka50_cockpit_l` | broken, rpm2, rotor_broken, depth, Distance, overload, zoom, cockpit_open, load |
| `event:/aircraft/engines/engine_ka50_cockpit_r` | load, cockpit_open, overload, zoom, Distance, rpm2, broken, rotor_broken |
| `event:/aircraft/engines/engine_ka50_l` | rotor_broken, broken, rpm2, Distance, depth, zoom, Event Cone Angle, load |
| `event:/aircraft/engines/engine_ka50_prop_cockpit_l` | load, cockpit_open, rpm, Distance, rotor_broken, broken |
| `event:/aircraft/engines/engine_ka50_prop_cockpit_r` | rpm, load, cockpit_open, broken, rotor_broken, Distance |
| `event:/aircraft/engines/engine_ka50_prop_l` | broken, rotor_broken, depth, event_vertical_angle, Distance, rpm, load, Event Cone Angle |
| `event:/aircraft/engines/engine_ka50_prop_r` | event_vertical_angle, Distance, broken, rotor_broken, load, Event Cone Angle, rpm |
| `event:/aircraft/engines/engine_ka50_r` | broken, rpm2, rotor_broken, Distance, zoom, load, Event Cone Angle |
| `event:/aircraft/engines/engine_ka50_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_ka50_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_ka50_start_l` | Distance |
| `event:/aircraft/engines/engine_ka50_start_r` | Distance |
| `event:/aircraft/engines/engine_ka50_stop_cockpit_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_ka50_stop_cockpit_r` | rpm2, Distance |
| `event:/aircraft/engines/engine_ka50_stop_l` | rpm2, Distance |
| `event:/aircraft/engines/engine_ka50_stop_r` | Distance, rpm2 |
| `event:/aircraft/engines/engine_mi24v_cockpit_l` | load, cockpit_open, zoom, overload, Distance, depth, rotor_broken, rpm2, broken |
| `event:/aircraft/engines/engine_mi24v_cockpit_r` | Distance, rpm2, broken, rotor_broken, load, cockpit_open, overload, zoom |
| `event:/aircraft/engines/engine_mi24v_l` | Distance, depth, rotor_broken, broken, rpm2, Event Cone Angle, load, zoom |
| `event:/aircraft/engines/engine_mi24v_prop_cockpit_l` | rotor_broken, broken, Distance, rpm, load, cockpit_open |
| `event:/aircraft/engines/engine_mi24v_prop_cockpit_r` | load, cockpit_open, rpm, Distance, rotor_broken, broken |
| `event:/aircraft/engines/engine_mi24v_prop_l` | depth, Distance, broken, rotor_broken, load, Event Cone Angle, rpm |
| `event:/aircraft/engines/engine_mi24v_prop_r` | Event Cone Angle, load, rpm, Distance, rotor_broken, broken |
| `event:/aircraft/engines/engine_mi24v_r` | Distance, rotor_broken, rpm2, broken, Event Cone Angle, load, zoom |
| `event:/aircraft/engines/engine_mi24v_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_mi24v_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_mi24v_start_l` | Distance |
| `event:/aircraft/engines/engine_mi24v_start_r` | Distance |
| `event:/aircraft/engines/engine_mi24v_stop_cockpit_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_mi24v_stop_cockpit_r` | Distance, rpm2 |
| `event:/aircraft/engines/engine_mi24v_stop_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_mi24v_stop_r` | rpm2, Distance |
| `event:/aircraft/engines/engine_mi4` | load, Event Cone Angle, rpm, zoom, depth, Distance, broken, rotor_broken |
| `event:/aircraft/engines/engine_mi4_ai` | Direction, is_enemy, is_visible, Distance, rpm, headphones, Event Cone Angle, Elevation, load |
| `event:/aircraft/engines/engine_mi4_ai_start` | headphones, Distance, Elevation, is_enemy, Direction, listener_is_ground, is_visible |
| `event:/aircraft/engines/engine_mi4_ai_stop` | is_enemy, Direction, listener_is_ground, is_visible, headphones, Distance, Elevation, Event Cone Angle |
| `event:/aircraft/engines/engine_mi4_cockpit_l` | rotor_broken, broken, Distance, depth, overload, zoom, rpm, load, cockpit_open |
| `event:/aircraft/engines/engine_mi4_cockpit_r` | load, cockpit_open, zoom, overload, rpm, Distance, rotor_broken, broken |
| `event:/aircraft/engines/engine_mi4_prop` | rotor_broken, Distance, rpm, Event Cone Angle |
| `event:/aircraft/engines/engine_mi4_prop_cockpit_l` | Distance, rotor_broken, load, cockpit_open, rpm, broken |
| `event:/aircraft/engines/engine_mi4_prop_cockpit_r` | Distance, rotor_broken, cockpit_open, load, rpm, broken |
| `event:/aircraft/engines/engine_mi4_start` | Distance |
| `event:/aircraft/engines/engine_mi4_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_mi4_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_mi4_stop` | Distance, Event Cone Angle |
| `event:/aircraft/engines/engine_mi4_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine_mi4_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine_mi_8t_cockpit_l` | depth, Distance, rpm2, broken, rotor_broken, load, cockpit_open, zoom, overload |
| `event:/aircraft/engines/engine_mi_8t_cockpit_r` | broken, rpm2, rotor_broken, Distance, zoom, overload, cockpit_open, load |
| `event:/aircraft/engines/engine_mi_8t_l` | load, Event Cone Angle, zoom, depth, Distance, rpm2, broken, rotor_broken |
| `event:/aircraft/engines/engine_mi_8t_prop_cockpit_l` | Distance, rotor_broken, broken, load, cockpit_open, rpm |
| `event:/aircraft/engines/engine_mi_8t_prop_cockpit_r` | rpm, load, cockpit_open, rotor_broken, broken, Distance |
| `event:/aircraft/engines/engine_mi_8t_prop_l` | rpm, Event Cone Angle, load, rotor_broken, broken, Distance, depth |
| `event:/aircraft/engines/engine_mi_8t_prop_r` | Distance, broken, rotor_broken, load, Event Cone Angle, rpm |
| `event:/aircraft/engines/engine_mi_8t_r` | zoom, load, Event Cone Angle, rpm2, broken, rotor_broken, Distance |
| `event:/aircraft/engines/engine_mi_8t_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_mi_8t_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_mi_8t_start_l` | Distance |
| `event:/aircraft/engines/engine_mi_8t_start_r` | Distance |
| `event:/aircraft/engines/engine_mi_8t_stop_cockpit_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_mi_8t_stop_cockpit_r` | Distance, rpm2 |
| `event:/aircraft/engines/engine_mi_8t_stop_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_mi_8t_stop_r` | Distance, rpm2 |
| `event:/aircraft/engines/engine_oh_58d` | Distance, depth, rotor_broken, broken, rpm2, Event Cone Angle, load, zoom |
| `event:/aircraft/engines/engine_oh_58d_cockpit_l` | rpm2, broken, rotor_broken, depth, Distance, zoom, overload, load, cockpit_open |
| `event:/aircraft/engines/engine_oh_58d_cockpit_r` | Distance, rotor_broken, rpm2, broken, load, cockpit_open, overload, zoom |
| `event:/aircraft/engines/engine_oh_58d_prop` | overload, rpm, Event Cone Angle, rotor_broken, Distance |
| `event:/aircraft/engines/engine_oh_58d_prop_cockpit_l` | rpm, broken, load, cockpit_open, rotor_broken, Distance |
| `event:/aircraft/engines/engine_oh_58d_prop_cockpit_r` | broken, rpm, cockpit_open, load, rotor_broken, Distance |
| `event:/aircraft/engines/engine_oh_58d_start` | Distance |
| `event:/aircraft/engines/engine_oh_58d_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_oh_58d_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_oh_58d_stop` | rpm2, Distance |
| `event:/aircraft/engines/engine_oh_58d_stop_cockpit_l` | rpm2, Distance |
| `event:/aircraft/engines/engine_oh_58d_stop_cockpit_r` | rpm2, Distance |
| `event:/aircraft/engines/engine_piston_corsair_far_ai` | listener_is_ground, Direction, Distance, rpm, Event Cone Angle, load |
| `event:/aircraft/engines/engine_piston_far_ai` | Distance, rpm, Event Cone Angle, load, Direction, listener_is_ground |
| `event:/aircraft/engines/engine_piston_mustang_far_ai` | Event Cone Angle, Distance, rpm, load, Direction, listener_is_ground |
| `event:/aircraft/engines/engine_quing_6` | overload, zoom, load, rpm, Event Cone Angle, rpm2, broken, depth, event_vertical_angle, Distance |
| `event:/aircraft/engines/engine_quing_6_ai` | Direction, rpm2, is_enemy, is_visible, speed_relative, listener_is_ground, headphones, rpm, Distance, Event Cone Angle, Elevation, load |
| `event:/aircraft/engines/engine_quing_6_cockpit_l` | broken, rpm2, Distance, depth, zoom, overload, cockpit_open, load |
| `event:/aircraft/engines/engine_quing_6_cockpit_r` | broken, rpm2, Distance, zoom, overload, cockpit_open, load |
| `event:/aircraft/engines/engine_quing_6_prop` | Distance |
| `event:/aircraft/engines/engine_quing_6_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine_quing_6_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine_quing_6_start` | load, Event Cone Angle, Distance |
| `event:/aircraft/engines/engine_quing_6_start_cockpit_l` | load |
| `event:/aircraft/engines/engine_quing_6_start_cockpit_r` | load |
| `event:/aircraft/engines/engine_quing_6_stop` | zoom, load, Event Cone Angle, rpm2, broken, Distance |
| `event:/aircraft/engines/engine_quing_6_stop_cockpit_l` | Distance, rpm2, cockpit_open, rpm, zoom |
| `event:/aircraft/engines/engine_quing_6_stop_cockpit_r` | Distance, rpm2, cockpit_open, zoom |
| `event:/aircraft/engines/engine_rah_66_cockpit_l` | depth, Distance, broken, rpm2, rotor_broken, cockpit_open, load, zoom, overload |
| `event:/aircraft/engines/engine_rah_66_cockpit_r` | zoom, overload, load, cockpit_open, rpm2, broken, rotor_broken, Distance |
| `event:/aircraft/engines/engine_rah_66_l` | depth, Distance, rpm2, broken, rotor_broken, load, Event Cone Angle, zoom |
| `event:/aircraft/engines/engine_rah_66_prop_cockpit_l` | Distance, rotor_broken, load, cockpit_open, rpm |
| `event:/aircraft/engines/engine_rah_66_prop_cockpit_r` | load, cockpit_open, rpm, Distance, rotor_broken |
| `event:/aircraft/engines/engine_rah_66_prop_l` | Event Cone Angle, rpm, Distance, rotor_broken |
| `event:/aircraft/engines/engine_rah_66_prop_r` | Distance, rotor_broken, Event Cone Angle, rpm |
| `event:/aircraft/engines/engine_rah_66_r` | Distance, rotor_broken, broken, rpm2, Event Cone Angle, load, zoom |
| `event:/aircraft/engines/engine_rah_66_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_rah_66_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_rah_66_start_l` | Distance |
| `event:/aircraft/engines/engine_rah_66_start_r` | Distance |
| `event:/aircraft/engines/engine_rah_66_stop_cockpit_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_rah_66_stop_cockpit_r` | rpm2, Distance |
| `event:/aircraft/engines/engine_rah_66_stop_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_rah_66_stop_r` | Distance, rpm2 |
| `event:/aircraft/engines/engine_sa_313b` | rotor_broken, rpm2, broken, Distance, load, depth, zoom, Event Cone Angle, cockpit_open |
| `event:/aircraft/engines/engine_sa_313b_cockpit_l` | cockpit_open, load, overload, zoom, depth, Distance, broken, rpm2, rotor_broken |
| `event:/aircraft/engines/engine_sa_313b_cockpit_r` | load, cockpit_open, overload, zoom, Distance, rpm2, broken, rotor_broken |
| `event:/aircraft/engines/engine_sa_313b_prop` | rotor_broken, Distance, rpm, Event Cone Angle |
| `event:/aircraft/engines/engine_sa_313b_prop_cockpit_l` | Distance, rotor_broken, cockpit_open, load, rpm, broken |
| `event:/aircraft/engines/engine_sa_313b_prop_cockpit_r` | rotor_broken, Distance, rpm, broken, cockpit_open, load |
| `event:/aircraft/engines/engine_sa_313b_start` | Distance |
| `event:/aircraft/engines/engine_sa_313b_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_sa_313b_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_sa_313b_stop` | rpm2, Distance |
| `event:/aircraft/engines/engine_sa_313b_stop_cockpit_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_sa_313b_stop_cockpit_r` | rpm2, Distance |
| `event:/aircraft/engines/engine_tiger_cockpit_l` | depth, Distance, broken, rpm2, rotor_broken, cockpit_open, load, zoom, overload |
| `event:/aircraft/engines/engine_tiger_cockpit_r` | Distance, rotor_broken, rpm2, broken, load, cockpit_open, zoom, overload |
| `event:/aircraft/engines/engine_tiger_l` | broken, rpm2, rotor_broken, depth, Distance, zoom, load, Event Cone Angle |
| `event:/aircraft/engines/engine_tiger_prop_cockpit_l` | rpm, load, cockpit_open, rotor_broken, Distance |
| `event:/aircraft/engines/engine_tiger_prop_cockpit_r` | load, cockpit_open, rpm, Distance, rotor_broken |
| `event:/aircraft/engines/engine_tiger_prop_l` | rotor_broken, Distance, rpm, Event Cone Angle |
| `event:/aircraft/engines/engine_tiger_prop_r` | rotor_broken, Distance, rpm, Event Cone Angle |
| `event:/aircraft/engines/engine_tiger_r` | rotor_broken, rpm2, broken, Distance, zoom, Event Cone Angle, load |
| `event:/aircraft/engines/engine_tiger_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_tiger_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_tiger_start_l` | Distance |
| `event:/aircraft/engines/engine_tiger_start_r` | Distance |
| `event:/aircraft/engines/engine_tiger_stop_cockpit_l` | rpm2, Distance |
| `event:/aircraft/engines/engine_tiger_stop_cockpit_r` | rpm2, Distance |
| `event:/aircraft/engines/engine_tiger_stop_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_tiger_stop_r` | rpm2, Distance |
| `event:/aircraft/engines/engine_tvd_ai_start` | Distance |
| `event:/aircraft/engines/engine_tvd_ai_stop` | Distance |
| `event:/aircraft/engines/engine_tvd_far_ai` | load, Event Cone Angle, Distance, listener_is_ground, rpm2, Direction |
| `event:/aircraft/engines/engine_uav` | Distance, rpm, event_vertical_angle, depth, overload, Event Cone Angle, load, zoom |
| `event:/aircraft/engines/engine_uav_ai` | Event Cone Angle, Elevation, Distance, load, headphones, rpm, is_visible, speed_relative, listener_is_ground, overload, Direction, is_enemy |
| `event:/aircraft/engines/engine_uav_mq1` | overload, depth, event_vertical_angle, rpm, Distance, zoom, load, Event Cone Angle |
| `event:/aircraft/engines/engine_uav_mq1_ai` | Distance, Elevation, Event Cone Angle, load, headphones, is_visible, rpm, listener_is_ground, speed_relative, Direction, overload, is_enemy |
| `event:/aircraft/engines/engine_uav_mq1_prop` | Distance |
| `event:/aircraft/engines/engine_uav_mq1_start` | Distance |
| `event:/aircraft/engines/engine_uav_mq1_stop` | Distance |
| `event:/aircraft/engines/engine_uav_prop` | Distance |
| `event:/aircraft/engines/engine_uav_start` | Distance |
| `event:/aircraft/engines/engine_uav_stop` | Distance |
| `event:/aircraft/engines/engine_uh_1` | zoom, load, Event Cone Angle, rpm2, broken, rotor_broken, depth, Distance |
| `event:/aircraft/engines/engine_uh_1_cockpit_l` | Distance, depth, rotor_broken, broken, rpm2, cockpit_open, load, zoom, overload |
| `event:/aircraft/engines/engine_uh_1_cockpit_r` | Distance, rotor_broken, broken, rpm2, cockpit_open, load, overload, zoom |
| `event:/aircraft/engines/engine_uh_1_prop` | broken, rpm, Event Cone Angle, load, rotor_broken, Distance, depth |
| `event:/aircraft/engines/engine_uh_1_prop_cockpit_l` | rotor_broken, broken, Distance, rpm, cockpit_open, load |
| `event:/aircraft/engines/engine_uh_1_prop_cockpit_r` | rpm, cockpit_open, load, broken, rotor_broken, Distance |
| `event:/aircraft/engines/engine_uh_1_start` | Distance |
| `event:/aircraft/engines/engine_uh_1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_uh_1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_uh_1_stop` | Distance, rpm2 |
| `event:/aircraft/engines/engine_uh_1_stop_cockpit_l` | rpm2, Distance |
| `event:/aircraft/engines/engine_uh_1_stop_cockpit_r` | rpm2, Distance |
| `event:/aircraft/engines/engine_uh_60_cockpit_l` | depth, Distance, broken, rpm2, rotor_broken, cockpit_open, load, zoom, overload |
| `event:/aircraft/engines/engine_uh_60_cockpit_r` | rotor_broken, rpm2, broken, Distance, zoom, overload, load, cockpit_open |
| `event:/aircraft/engines/engine_uh_60_l` | depth, Distance, broken, rpm2, rotor_broken, load, Event Cone Angle, zoom |
| `event:/aircraft/engines/engine_uh_60_prop_cockpit_l` | rpm, cockpit_open, load, broken, rotor_broken, Distance |
| `event:/aircraft/engines/engine_uh_60_prop_cockpit_r` | cockpit_open, load, rpm, Distance, rotor_broken, broken |
| `event:/aircraft/engines/engine_uh_60_prop_l` | broken, rpm, Event Cone Angle, load, rotor_broken, Distance, depth |
| `event:/aircraft/engines/engine_uh_60_prop_r` | load, Event Cone Angle, broken, rpm, depth, Distance, rotor_broken |
| `event:/aircraft/engines/engine_uh_60_r` | zoom, Event Cone Angle, load, rotor_broken, rpm2, broken, Distance, depth |
| `event:/aircraft/engines/engine_uh_60_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_uh_60_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_uh_60_start_l` | Distance |
| `event:/aircraft/engines/engine_uh_60_start_r` | Distance |
| `event:/aircraft/engines/engine_uh_60_stop_cockpit_l` | rpm2, Distance |
| `event:/aircraft/engines/engine_uh_60_stop_cockpit_r` | Distance, rpm2 |
| `event:/aircraft/engines/engine_uh_60_stop_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_uh_60_stop_r` | Distance, rpm2 |
| `event:/aircraft/engines/engine_wessex_mk5_cockpit_l` | rotor_broken, broken, rpm2, Distance, depth, zoom, overload, cockpit_open, load |
| `event:/aircraft/engines/engine_wessex_mk5_cockpit_r` | cockpit_open, load, zoom, overload, Distance, rotor_broken, broken, rpm2 |
| `event:/aircraft/engines/engine_wessex_mk5_l` | load, Event Cone Angle, zoom, depth, Distance, rpm2, broken, rotor_broken |
| `event:/aircraft/engines/engine_wessex_mk5_prop_cockpit_l` | rpm, load, cockpit_open, rotor_broken, broken, Distance |
| `event:/aircraft/engines/engine_wessex_mk5_prop_cockpit_r` | load, cockpit_open, rpm, Distance, rotor_broken, broken |
| `event:/aircraft/engines/engine_wessex_mk5_prop_l` | broken, rpm, Event Cone Angle, load, rotor_broken, Distance, depth |
| `event:/aircraft/engines/engine_wessex_mk5_prop_r` | depth, Distance, broken, rotor_broken, load, Event Cone Angle, rpm |
| `event:/aircraft/engines/engine_wessex_mk5_r` | Event Cone Angle, load, zoom, Distance, depth, rotor_broken, rpm2, broken |
| `event:/aircraft/engines/engine_wessex_mk5_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_wessex_mk5_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_wessex_mk5_start_l` | Distance |
| `event:/aircraft/engines/engine_wessex_mk5_start_r` | Distance |
| `event:/aircraft/engines/engine_wessex_mk5_stop_cockpit_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_wessex_mk5_stop_cockpit_r` | rpm2, Distance |
| `event:/aircraft/engines/engine_wessex_mk5_stop_l` | rpm2, Distance |
| `event:/aircraft/engines/engine_wessex_mk5_stop_r` | rpm2, Distance |
| `event:/aircraft/engines/engine_xf5u1` | Event Cone Angle, rpm, load, zoom, overload, Distance, depth, event_vertical_angle |
| `event:/aircraft/engines/engine_xf5u1_ai` | headphones, Event Cone Angle, Elevation, rpm, Distance, load, Direction, is_enemy, is_visible, speed_relative, listener_is_ground |
| `event:/aircraft/engines/engine_xf5u1_cockpit_l` | Distance, depth, rpm, cockpit_open, load, zoom, overload |
| `event:/aircraft/engines/engine_xf5u1_cockpit_r` | Distance, cockpit_open, load, rpm, zoom, overload |
| `event:/aircraft/engines/engine_xf5u1_prop` | Distance |
| `event:/aircraft/engines/engine_xf5u1_prop_cockpit_l` | loop, Distance |
| `event:/aircraft/engines/engine_xf5u1_prop_cockpit_r` | Distance, loop |
| `event:/aircraft/engines/engine_xf5u1_start` | Distance |
| `event:/aircraft/engines/engine_xf5u1_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_xf5u1_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_xf5u1_stop` | Distance |
| `event:/aircraft/engines/engine_xf5u1_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine_xf5u1_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine_xp55` | load, Event Cone Angle, rpm, zoom, overload, event_vertical_angle, depth, Distance |
| `event:/aircraft/engines/engine_xp55_ai` | Direction, is_enemy, is_visible, listener_is_ground, speed_relative, headphones, Elevation, Event Cone Angle, Distance, rpm, load |
| `event:/aircraft/engines/engine_xp55_cockpit_l` | Distance, depth, rpm, cockpit_open, load, overload, zoom |
| `event:/aircraft/engines/engine_xp55_cockpit_r` | rpm, load, cockpit_open, overload, zoom, Distance |
| `event:/aircraft/engines/engine_xp55_prop` | Distance |
| `event:/aircraft/engines/engine_xp55_prop_cockpit_l` | Distance, loop |
| `event:/aircraft/engines/engine_xp55_prop_cockpit_r` | loop, Distance |
| `event:/aircraft/engines/engine_xp55_start` | Distance |
| `event:/aircraft/engines/engine_xp55_start_cockpit_l` | Distance |
| `event:/aircraft/engines/engine_xp55_start_cockpit_r` | Distance |
| `event:/aircraft/engines/engine_xp55_stop` | Distance |
| `event:/aircraft/engines/engine_xp55_stop_cockpit_l` |  |
| `event:/aircraft/engines/engine_xp55_stop_cockpit_r` |  |
| `event:/aircraft/engines/engine_z19_cockpit_l` | zoom, overload, load, cockpit_open, rpm2, broken, rotor_broken, depth, Distance |
| `event:/aircraft/engines/engine_z19_cockpit_r` | zoom, overload, cockpit_open, load, rotor_broken, broken, rpm2, Distance |
| `event:/aircraft/engines/engine_z19_l` | depth, Distance, broken, rpm2, rotor_broken, load, Event Cone Angle, zoom |
| `event:/aircraft/engines/engine_z19_prop_cockpit_l` | rpm, cockpit_open, load, rotor_broken, Distance |
| `event:/aircraft/engines/engine_z19_prop_cockpit_r` | rotor_broken, Distance, rpm, cockpit_open, load |
| `event:/aircraft/engines/engine_z19_prop_l` | rotor_broken, Distance, rpm, Event Cone Angle |
| `event:/aircraft/engines/engine_z19_prop_r` | rotor_broken, Distance, rpm, Event Cone Angle |
| `event:/aircraft/engines/engine_z19_r` | rotor_broken, rpm2, broken, Distance, zoom, Event Cone Angle, load |
| `event:/aircraft/engines/engine_z19_start_cockpit_l` |  |
| `event:/aircraft/engines/engine_z19_start_cockpit_r` |  |
| `event:/aircraft/engines/engine_z19_start_l` | Distance |
| `event:/aircraft/engines/engine_z19_start_r` | Distance |
| `event:/aircraft/engines/engine_z19_stop_cockpit_l` | rpm2, Distance |
| `event:/aircraft/engines/engine_z19_stop_cockpit_r` | rpm2, Distance |
| `event:/aircraft/engines/engine_z19_stop_l` | Distance, rpm2 |
| `event:/aircraft/engines/engine_z19_stop_r` | rpm2, Distance |
| `event:/aircraft/engines/rotor20` | Event Cone Angle, load, rpm, broken, zoom, Distance, depth |
| `event:/aircraft/engines/rotor20_ai` | rpm, headphones, load, Event Cone Angle, Elevation, Distance, is_enemy, Direction, listener_is_ground, is_visible |
| `event:/aircraft/engines/rotor20_cockpit` | Distance, cockpit_open, load, rpm, overload, zoom |
| `event:/aircraft/engines/rotor_ah56` | depth, event_vertical_angle, Distance, rpm, broken, overload, zoom, load, Event Cone Angle |
| `event:/aircraft/engines/rotor_ah56_ai` | is_enemy, Direction, rpm, is_visible, broken, headphones, Distance, load, Event Cone Angle, Elevation |
| `event:/aircraft/engines/rotor_ah56_cockpit_l` | rpm, broken, zoom, overload, cockpit_open, load, Distance |
| `event:/aircraft/engines/rotor_ah56_cockpit_r` | rpm, broken, zoom, overload, cockpit_open, load, Distance |
| `event:/aircraft/engines/rotor_ah56_tail` | load, Event Cone Angle, broken, rpm, depth, Distance, rotor_broken |
| `event:/aircraft/engines/rotor_ah64` | depth, event_vertical_angle, Distance, load, Event Cone Angle, overload, zoom, broken, rpm |
| `event:/aircraft/engines/rotor_ah64_ai` | Distance, broken, headphones, Elevation, Event Cone Angle, load, rpm, Direction, is_enemy, is_visible |
| `event:/aircraft/engines/rotor_ah64_cockpit_l` | Distance, load, cockpit_open, zoom, overload, rpm, broken |
| `event:/aircraft/engines/rotor_ah64_cockpit_r` | Distance, cockpit_open, load, rpm, broken, overload, zoom |
| `event:/aircraft/engines/rotor_ah64_tail` | rpm, broken, Event Cone Angle, load, rotor_broken, Distance, depth |
| `event:/aircraft/engines/rotor_bo_105` | Event Cone Angle, load, overload, rpm, broken, Distance, event_vertical_angle, depth |
| `event:/aircraft/engines/rotor_bo_105_ai` | Distance, headphones, broken, Event Cone Angle, Elevation, load, rpm, Direction, is_enemy, is_visible |
| `event:/aircraft/engines/rotor_bo_105_cockpit_l` | broken, rpm, cockpit_open, load |
| `event:/aircraft/engines/rotor_bo_105_cockpit_r` | cockpit_open, load, broken, rpm |
| `event:/aircraft/engines/rotor_bo_105_tail` | load, Event Cone Angle, rpm, broken, depth, Distance, rotor_broken |
| `event:/aircraft/engines/rotor_echo_ah56` | depth, Distance, broken, rpm, load, Event Cone Angle |
| `event:/aircraft/engines/rotor_echo_ah64` | depth, Distance, rpm, broken, load, Event Cone Angle |
| `event:/aircraft/engines/rotor_echo_bo_105` | rpm, broken, load, Event Cone Angle, depth, Distance |
| `event:/aircraft/engines/rotor_echo_ka50` | Event Cone Angle, load, broken, rpm, Distance, depth, rotor_broken |
| `event:/aircraft/engines/rotor_echo_mi24v` | load, Event Cone Angle, rpm, broken, depth, Distance |
| `event:/aircraft/engines/rotor_echo_mi4` | load, Event Cone Angle, broken, rpm, depth, Distance |
| `event:/aircraft/engines/rotor_echo_mi_8t` | load, Event Cone Angle, broken, rpm, depth, Distance |
| `event:/aircraft/engines/rotor_echo_oh_58d` | depth, Distance, load, Event Cone Angle, rpm, broken |
| `event:/aircraft/engines/rotor_echo_rah_66` | depth, Distance, rpm, broken, load, Event Cone Angle |
| `event:/aircraft/engines/rotor_echo_sa_313b` | Distance, depth, Event Cone Angle, load, broken, rpm |
| `event:/aircraft/engines/rotor_echo_tiger` | Distance, depth, Event Cone Angle, load, broken, rpm |
| `event:/aircraft/engines/rotor_echo_uh_1` | depth, Distance, broken, rpm, load, Event Cone Angle |
| `event:/aircraft/engines/rotor_echo_uh_60` | depth, Distance, rpm, broken, load, Event Cone Angle |
| `event:/aircraft/engines/rotor_echo_wessex_mk5` | depth, Distance, load, Event Cone Angle, rpm, broken |
| `event:/aircraft/engines/rotor_echo_z19` | Distance, depth, Event Cone Angle, load, rpm, broken |
| `event:/aircraft/engines/rotor_heli_ai` | Elevation, Event Cone Angle, Distance, load, broken, headphones, is_visible, Direction, rpm, is_enemy |
| `event:/aircraft/engines/rotor_heli_blades_ai` | is_visible, rpm, Direction, is_enemy, Distance, Elevation, Event Cone Angle, load, headphones, broken |
| `event:/aircraft/engines/rotor_heli_piston_ai` | rpm, Direction, is_enemy, is_visible, Distance, broken, headphones, Event Cone Angle, Elevation, load |
| `event:/aircraft/engines/rotor_heli_small_ai` | is_visible, rpm, Direction, is_enemy, Distance, Event Cone Angle, Elevation, load, headphones, broken |
| `event:/aircraft/engines/rotor_ka50` | Event Cone Angle, load, overload, rpm, broken, Distance, depth, event_vertical_angle |
| `event:/aircraft/engines/rotor_ka50_ai` | load, Event Cone Angle, Elevation, Distance, broken, headphones, is_visible, is_enemy, rpm, Direction |
| `event:/aircraft/engines/rotor_ka50_cockpit_l` | Distance, rpm, broken, cockpit_open, load |
| `event:/aircraft/engines/rotor_ka50_cockpit_r` | Distance, broken, rpm, cockpit_open, load |
| `event:/aircraft/engines/rotor_mi24v` | overload, rpm, broken, Event Cone Angle, load, Distance, event_vertical_angle, depth |
| `event:/aircraft/engines/rotor_mi24v_ai` | Direction, rpm, is_enemy, is_visible, Distance, broken, headphones, Elevation, Event Cone Angle, load |
| `event:/aircraft/engines/rotor_mi24v_cockpit_l` | rpm, broken, cockpit_open, load, Distance |
| `event:/aircraft/engines/rotor_mi24v_cockpit_r` | broken, rpm, load, cockpit_open, Distance |
| `event:/aircraft/engines/rotor_mi24v_tail` | rotor_broken, Distance, depth, broken, rpm, Event Cone Angle, load |
| `event:/aircraft/engines/rotor_mi4` | depth, event_vertical_angle, Distance, load, Event Cone Angle, overload, zoom, broken, rpm |
| `event:/aircraft/engines/rotor_mi4_ai` | is_enemy, rpm, Direction, is_visible, headphones, broken, Distance, load, Event Cone Angle, Elevation |
| `event:/aircraft/engines/rotor_mi4_cockpit_l` | Distance, broken, rpm, zoom, overload, cockpit_open, load |
| `event:/aircraft/engines/rotor_mi4_cockpit_r` | Distance, zoom, overload, broken, rpm, load, cockpit_open |
| `event:/aircraft/engines/rotor_mi4_tail` | rotor_broken, Distance, depth, rpm, broken, Event Cone Angle, load |
| `event:/aircraft/engines/rotor_mi_8t` | rpm, broken, overload, load, Event Cone Angle, event_vertical_angle, depth, Distance |
| `event:/aircraft/engines/rotor_mi_8t_ai` | Distance, headphones, broken, Elevation, Event Cone Angle, load, rpm, Direction, is_enemy, is_visible |
| `event:/aircraft/engines/rotor_mi_8t_cockpit_l` | Distance, rpm, broken, cockpit_open, load |
| `event:/aircraft/engines/rotor_mi_8t_cockpit_r` | Distance, broken, rpm, cockpit_open, load |
| `event:/aircraft/engines/rotor_mi_8t_tail` | rotor_broken, Distance, depth, broken, rpm, Event Cone Angle, load |
| `event:/aircraft/engines/rotor_oh_58d` | load, Event Cone Angle, overload, rpm, broken, event_vertical_angle, depth, Distance |
| `event:/aircraft/engines/rotor_oh_58d_ai` | load, Event Cone Angle, Elevation, Distance, broken, headphones, is_visible, is_enemy, Direction, rpm |
| `event:/aircraft/engines/rotor_oh_58d_cockpit_l` | cockpit_open, load, rpm, broken, Distance |
| `event:/aircraft/engines/rotor_oh_58d_cockpit_r` | load, cockpit_open, broken, rpm, Distance |
| `event:/aircraft/engines/rotor_oh_58d_tail` | broken, rpm, load, Event Cone Angle, rotor_broken, depth, Distance |
| `event:/aircraft/engines/rotor_quing_6` | broken, rpm, zoom, load, Event Cone Angle, depth, Distance |
| `event:/aircraft/engines/rotor_quing_6_ai` | Distance, Elevation, Event Cone Angle, load, headphones, rpm, is_visible, listener_is_ground, Direction, is_enemy |
| `event:/aircraft/engines/rotor_quing_6_cockpit` | overload, zoom, rpm, load, cockpit_open, rpm2, Distance |
| `event:/aircraft/engines/rotor_rah_66` | event_vertical_angle, depth, Distance, load, Event Cone Angle, overload, zoom, broken, rpm |
| `event:/aircraft/engines/rotor_rah_66_ai` | Distance, broken, headphones, Elevation, Event Cone Angle, load, Direction, rpm, is_enemy, is_visible |
| `event:/aircraft/engines/rotor_rah_66_cockpit_l` | Distance, rpm, broken, zoom, overload, cockpit_open, load |
| `event:/aircraft/engines/rotor_rah_66_cockpit_r` | overload, zoom, broken, rpm, load, cockpit_open, Distance |
| `event:/aircraft/engines/rotor_rah_66_tail` | Event Cone Angle, load, broken, rpm, Distance, depth, rotor_broken |
| `event:/aircraft/engines/rotor_sa_313b` | event_vertical_angle, depth, Distance, rpm, broken, overload, zoom, load, Event Cone Angle |
| `event:/aircraft/engines/rotor_sa_313b_ai` | headphones, broken, Distance, load, Event Cone Angle, Elevation, is_enemy, Direction, rpm, is_visible |
| `event:/aircraft/engines/rotor_sa_313b_cockpit_l` | rpm2, Distance, broken, rpm, overload, zoom, cockpit_open, load |
| `event:/aircraft/engines/rotor_sa_313b_cockpit_r` | rpm2, Distance, rpm, broken, zoom, overload, cockpit_open, load |
| `event:/aircraft/engines/rotor_sa_313b_tail` | rpm, broken, Event Cone Angle, load, rotor_broken, Distance, depth |
| `event:/aircraft/engines/rotor_sa_341_ai` | is_visible, is_enemy, rpm, Direction, load, Distance, Event Cone Angle, Elevation, headphones, broken |
| `event:/aircraft/engines/rotor_tail` | Event Cone Angle, load, broken, rpm, Distance, depth, rotor_broken |
| `event:/aircraft/engines/rotor_tiger` | event_vertical_angle, depth, Distance, load, Event Cone Angle, overload, zoom, rpm, broken |
| `event:/aircraft/engines/rotor_tiger_ai` | broken, headphones, Distance, load, Elevation, Event Cone Angle, is_enemy, rpm, Direction, is_visible |
| `event:/aircraft/engines/rotor_tiger_cockpit_l` | load, cockpit_open, zoom, overload, broken, rpm, Distance |
| `event:/aircraft/engines/rotor_tiger_cockpit_r` | overload, zoom, rpm, broken, load, cockpit_open, Distance |
| `event:/aircraft/engines/rotor_tiger_tail` | broken, rpm, Event Cone Angle, load, rotor_broken, Distance, depth |
| `event:/aircraft/engines/rotor_uh_1` | load, Event Cone Angle, overload, broken, rpm, event_vertical_angle, depth, Distance |
| `event:/aircraft/engines/rotor_uh_1_ai` | Distance, headphones, broken, Elevation, Event Cone Angle, load, Direction, rpm, is_enemy, is_visible |
| `event:/aircraft/engines/rotor_uh_1_cockpit_l` | rpm, broken, cockpit_open, load, Distance |
| `event:/aircraft/engines/rotor_uh_1_cockpit_r` | rpm, broken, load, cockpit_open, Distance |
| `event:/aircraft/engines/rotor_uh_1_tail` | rotor_broken, depth, Distance, broken, rpm, load, Event Cone Angle |
| `event:/aircraft/engines/rotor_uh_60` | overload, rpm, broken, Event Cone Angle, load, Distance, depth, event_vertical_angle |
| `event:/aircraft/engines/rotor_uh_60_ai` | Distance, headphones, broken, Elevation, Event Cone Angle, load, Direction, rpm, is_enemy, is_visible |
| `event:/aircraft/engines/rotor_uh_60_cockpit_l` | broken, rpm, load, cockpit_open, Distance |
| `event:/aircraft/engines/rotor_uh_60_cockpit_r` | broken, rpm, cockpit_open, load, Distance |
| `event:/aircraft/engines/rotor_uh_60_tail` | Distance, depth, rotor_broken, Event Cone Angle, load, rpm, broken |
| `event:/aircraft/engines/rotor_wessex_mk5` | rpm, broken, overload, load, Event Cone Angle, event_vertical_angle, depth, Distance |
| `event:/aircraft/engines/rotor_wessex_mk5_ai` | is_visible, is_enemy, Direction, rpm, load, Distance, Elevation, Event Cone Angle, headphones, broken |
| `event:/aircraft/engines/rotor_wessex_mk5_cockpit_l` | Distance, cockpit_open, load, broken, rpm |
| `event:/aircraft/engines/rotor_wessex_mk5_cockpit_r` | rpm, broken, load, cockpit_open, Distance |
| `event:/aircraft/engines/rotor_wessex_mk5_tail` | rpm, broken, load, Event Cone Angle, rotor_broken, depth, Distance |
| `event:/aircraft/engines/rotor_z19` | load, Event Cone Angle, rpm, broken, overload, depth, event_vertical_angle, Distance |
| `event:/aircraft/engines/rotor_z19_ai` | load, Elevation, Event Cone Angle, Distance, broken, headphones, is_visible, is_enemy, rpm, Direction |
| `event:/aircraft/engines/rotor_z19_cockpit_l` | rpm, broken, cockpit_open, load, Distance |
| `event:/aircraft/engines/rotor_z19_cockpit_r` | load, cockpit_open, rpm, broken, Distance |
| `event:/aircraft/engines/rotor_z19_tail` | Distance, depth, rotor_broken, Event Cone Angle, load, rpm, broken |
| `event:/aircraft/engines/tank` | Distance, engine |
| `event:/aircraft/engines/truck` | engine, Distance |
| `event:/event/aircraft/engines/engine_zeppelin_far_ai` | rpm, Distance, Event Cone Angle, load, Direction, listener_is_ground |

## aircraft_gui

311 events (310 named), 408 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/aircraft/gui/alarm_alt` |  |
| `event:/aircraft/gui/alarm_attack_angle_f18` | intense |
| `event:/aircraft/gui/alarm_attack_angle_us` | intense |
| `event:/aircraft/gui/alarm_attack_angle_ussr_1` | intense |
| `event:/aircraft/gui/alarm_attack_angle_ussr_2` | intense |
| `event:/aircraft/gui/alarm_con_scan` | track |
| `event:/aircraft/gui/alarm_heatseeker_scan` | track |
| `event:/aircraft/gui/alarm_launch_detected` | volume |
| `event:/aircraft/gui/alarm_launch_detected_ch_mlws` | volume |
| `event:/aircraft/gui/alarm_launch_detected_ch_s740` | volume |
| `event:/aircraft/gui/alarm_launch_detected_fr_ddm2000` | volume |
| `event:/aircraft/gui/alarm_launch_detected_fr_spectra_mlws` | volume |
| `event:/aircraft/gui/alarm_launch_detected_il_paws_2` | volume |
| `event:/aircraft/gui/alarm_launch_detected_l150_lws` | volume |
| `event:/aircraft/gui/alarm_launch_detected_uk_praetorian_lws` | volume |
| `event:/aircraft/gui/alarm_launch_detected_us_an_aar_47` | volume |
| `event:/aircraft/gui/alarm_launch_detected_us_an_avr_2` | volume |
| `event:/aircraft/gui/alarm_radar` | track, launch, new, volume |
| `event:/aircraft/gui/alarm_radar_alr_67` | volume, launch, new, track |
| `event:/aircraft/gui/alarm_radar_alr_69` | track, volume, launch, new |
| `event:/aircraft/gui/alarm_radar_an_alr_46` | track, new, launch, volume |
| `event:/aircraft/gui/alarm_radar_an_alr_56` | new, launch, volume, track |
| `event:/aircraft/gui/alarm_radar_an_apr_39` | track, launch, new, volume |
| `event:/aircraft/gui/alarm_radar_an_aps_54` | launch, new, volume, track |
| `event:/aircraft/gui/alarm_radar_app_27` | volume, launch, new, track |
| `event:/aircraft/gui/alarm_radar_app_f9_5` | volume, launch, new, track |
| `event:/aircraft/gui/alarm_radar_apr25_ari18223` | track, volume, launch, new |
| `event:/aircraft/gui/alarm_radar_ar830` | track, volume, launch, new |
| `event:/aircraft/gui/alarm_radar_ari23333` | track, volume, launch, new |
| `event:/aircraft/gui/alarm_radar_j15d` | new, launch, volume, track |
| `event:/aircraft/gui/alarm_radar_kj8602` | volume, new, launch, track |
| `event:/aircraft/gui/alarm_radar_krkz2200` | volume, launch, new, track |
| `event:/aircraft/gui/alarm_radar_l150` | track, volume, new, launch |
| `event:/aircraft/gui/alarm_radar_mirage_3` | track, launch, new, volume |
| `event:/aircraft/gui/alarm_radar_praetorian` | track, launch, new, volume |
| `event:/aircraft/gui/alarm_radar_serval` | track, volume, launch, new |
| `event:/aircraft/gui/alarm_radar_sherloc` | volume, launch, new, track |
| `event:/aircraft/gui/alarm_radar_spectra` | launch, new, volume, track |
| `event:/aircraft/gui/alarm_radar_spo10` | track, volume, new, launch |
| `event:/aircraft/gui/alarm_radar_spo15lm` | launch, new, volume, track |
| `event:/aircraft/gui/alarm_radar_spo_2` | track, volume, new, launch |
| `event:/aircraft/gui/alarm_rocket` |  |
| `event:/aircraft/gui/alarm_spin_scan` | track |
| `event:/aircraft/gui/alarm_stall` | intense |
| `event:/aircraft/gui/alarm_stall_piston` | speed, overload, intense |
| `event:/aircraft/gui/alarm_wep` |  |
| `event:/aircraft/gui/bombs_reload` |  |
| `event:/aircraft/gui/chat_join` |  |
| `event:/aircraft/gui/chat_send` |  |
| `event:/aircraft/gui/chat_spam` |  |
| `event:/aircraft/gui/check` |  |
| `event:/aircraft/gui/chest_open` |  |
| `event:/aircraft/gui/choose` |  |
| `event:/aircraft/gui/click` |  |
| `event:/aircraft/gui/craft_event_capsule_landing` |  |
| `event:/aircraft/gui/craft_event_rocket_launch` |  |
| `event:/aircraft/gui/craft_event_win` |  |
| `event:/aircraft/gui/deb_achivement` |  |
| `event:/aircraft/gui/deb_count` |  |
| `event:/aircraft/gui/deb_medal` |  |
| `event:/aircraft/gui/deb_players_off` |  |
| `event:/aircraft/gui/deb_players_on` |  |
| `event:/aircraft/gui/enemy_ammo_burn` |  |
| `event:/aircraft/gui/enemy_citadel_breach` |  |
| `event:/aircraft/gui/enemy_destr_by_plane` |  |
| `event:/aircraft/gui/enemy_destr_by_ship` |  |
| `event:/aircraft/gui/enemy_destroyed` |  |
| `event:/aircraft/gui/enemy_kill_assist` |  |
| `event:/aircraft/gui/enemy_torpedo_hit` |  |
| `event:/aircraft/gui/focus` |  |
| `event:/aircraft/gui/gunner_injured` |  |
| `event:/aircraft/gui/gunner_out_of_ammo` |  |
| `event:/aircraft/gui/gunner_out_of_range` |  |
| `event:/aircraft/gui/gunner_reload` |  |
| `event:/aircraft/gui/gunner_reload_multiple` |  |
| `event:/aircraft/gui/kick_alert` |  |
| `event:/aircraft/gui/level_load_complete` |  |
| `event:/aircraft/gui/menu_appear` |  |
| `event:/aircraft/gui/minimap_off` |  |
| `event:/aircraft/gui/minimap_on` |  |
| `event:/aircraft/gui/mission_complete` |  |
| `event:/aircraft/gui/mission_failed` |  |
| `event:/aircraft/gui/new_rank` |  |
| `event:/aircraft/gui/next_target` |  |
| `event:/aircraft/gui/no_bullets` |  |
| `event:/aircraft/gui/obj_complete` |  |
| `event:/aircraft/gui/obj_failed` |  |
| `event:/aircraft/gui/obj_new` |  |
| `event:/aircraft/gui/obj_new3d` |  |
| `event:/aircraft/gui/obj_remind` |  |
| `event:/aircraft/gui/out_of_bombs` |  |
| `event:/aircraft/gui/out_of_rockets` |  |
| `event:/aircraft/gui/pip_appear` |  |
| `event:/aircraft/gui/roulette_spin` |  |
| `event:/aircraft/gui/roulette_start` |  |
| `event:/aircraft/gui/roulette_stop` |  |
| `event:/aircraft/gui/show_map` |  |
| `event:/aircraft/gui/slide_in` |  |
| `event:/aircraft/gui/slide_loop` |  |
| `event:/aircraft/gui/slide_out` |  |
| `event:/aircraft/gui/streak_mission_complete` |  |
| `event:/aircraft/gui/uncheck` |  |
| `event:/aircraft/gui/vws/betty/vws_ahead` |  |
| `event:/aircraft/gui/vws/betty/vws_airbrake` |  |
| `event:/aircraft/gui/vws/betty/vws_altitude` |  |
| `event:/aircraft/gui/vws/betty/vws_attack_air` |  |
| `event:/aircraft/gui/vws/betty/vws_attack_gepard` |  |
| `event:/aircraft/gui/vws/betty/vws_attack_sam` |  |
| `event:/aircraft/gui/vws/betty/vws_attack_stinger` |  |
| `event:/aircraft/gui/vws/betty/vws_behind` |  |
| `event:/aircraft/gui/vws/betty/vws_bingo` |  |
| `event:/aircraft/gui/vws/betty/vws_caution` |  |
| `event:/aircraft/gui/vws/betty/vws_chaff_flare` |  |
| `event:/aircraft/gui/vws/betty/vws_check_fuel` |  |
| `event:/aircraft/gui/vws/betty/vws_check_gear` |  |
| `event:/aircraft/gui/vws/betty/vws_check_mech` |  |
| `event:/aircraft/gui/vws/betty/vws_counter` |  |
| `event:/aircraft/gui/vws/betty/vws_critical_altitude` |  |
| `event:/aircraft/gui/vws/betty/vws_critical_angle` |  |
| `event:/aircraft/gui/vws/betty/vws_critical_engine_vibration` |  |
| `event:/aircraft/gui/vws/betty/vws_critical_left_engine_vibration` |  |
| `event:/aircraft/gui/vws/betty/vws_critical_right_engine_vibration` |  |
| `event:/aircraft/gui/vws/betty/vws_critical_speed` |  |
| `event:/aircraft/gui/vws/betty/vws_dangerous_close` |  |
| `event:/aircraft/gui/vws/betty/vws_dangerous_vibration` |  |
| `event:/aircraft/gui/vws/betty/vws_decrease_engine_rpm` |  |
| `event:/aircraft/gui/vws/betty/vws_decrease_left_engine_rpm` |  |
| `event:/aircraft/gui/vws/betty/vws_decrease_right_engine_rpm` |  |
| `event:/aircraft/gui/vws/betty/vws_eject` |  |
| `event:/aircraft/gui/vws/betty/vws_engine_failure` |  |
| `event:/aircraft/gui/vws/betty/vws_engine_fire` |  |
| `event:/aircraft/gui/vws/betty/vws_engine_fire_left` |  |
| `event:/aircraft/gui/vws/betty/vws_engine_fire_right` |  |
| `event:/aircraft/gui/vws/betty/vws_engine_overheat` |  |
| `event:/aircraft/gui/vws/betty/vws_fire` |  |
| `event:/aircraft/gui/vws/betty/vws_fuel_low` |  |
| `event:/aircraft/gui/vws/betty/vws_gear_down` |  |
| `event:/aircraft/gui/vws/betty/vws_generator_failure` |  |
| `event:/aircraft/gui/vws/betty/vws_high` |  |
| `event:/aircraft/gui/vws/betty/vws_hydrosystem_failure` |  |
| `event:/aircraft/gui/vws/betty/vws_increase_engine_rpm` |  |
| `event:/aircraft/gui/vws/betty/vws_jammer` |  |
| `event:/aircraft/gui/vws/betty/vws_left` |  |
| `event:/aircraft/gui/vws/betty/vws_left_engine_failure` |  |
| `event:/aircraft/gui/vws/betty/vws_left_engine_overheat` |  |
| `event:/aircraft/gui/vws/betty/vws_left_generator_failure` |  |
| `event:/aircraft/gui/vws/betty/vws_lock` |  |
| `event:/aircraft/gui/vws/betty/vws_lock_cockpit` |  |
| `event:/aircraft/gui/vws/betty/vws_low` |  |
| `event:/aircraft/gui/vws/betty/vws_main_gearbox_failure` |  |
| `event:/aircraft/gui/vws/betty/vws_missile` |  |
| `event:/aircraft/gui/vws/betty/vws_missile_launch` |  |
| `event:/aircraft/gui/vws/betty/vws_out` |  |
| `event:/aircraft/gui/vws/betty/vws_over_g` |  |
| `event:/aircraft/gui/vws/betty/vws_pull_up` |  |
| `event:/aircraft/gui/vws/betty/vws_right` |  |
| `event:/aircraft/gui/vws/betty/vws_right_engine_failure` |  |
| `event:/aircraft/gui/vws/betty/vws_right_engine_overheat` |  |
| `event:/aircraft/gui/vws/betty/vws_right_generator_failure` |  |
| `event:/aircraft/gui/vws/betty/vws_roll_left` |  |
| `event:/aircraft/gui/vws/betty/vws_roll_right` |  |
| `event:/aircraft/gui/vws/betty/vws_tailrotor_gearbox_failure` |  |
| `event:/aircraft/gui/vws/betty/vws_warning` |  |
| `event:/aircraft/gui/vws/rita/vws_ahead` |  |
| `event:/aircraft/gui/vws/rita/vws_airbrake` |  |
| `event:/aircraft/gui/vws/rita/vws_altitude` |  |
| `event:/aircraft/gui/vws/rita/vws_attack_air` |  |
| `event:/aircraft/gui/vws/rita/vws_attack_gepard` |  |
| `event:/aircraft/gui/vws/rita/vws_attack_sam` |  |
| `event:/aircraft/gui/vws/rita/vws_attack_stinger` |  |
| `event:/aircraft/gui/vws/rita/vws_behind` |  |
| `event:/aircraft/gui/vws/rita/vws_bingo` |  |
| `event:/aircraft/gui/vws/rita/vws_chaff_flare` |  |
| `event:/aircraft/gui/vws/rita/vws_check_fuel` |  |
| `event:/aircraft/gui/vws/rita/vws_check_gear` |  |
| `event:/aircraft/gui/vws/rita/vws_check_mech` |  |
| `event:/aircraft/gui/vws/rita/vws_counter` |  |
| `event:/aircraft/gui/vws/rita/vws_critical_altitude` |  |
| `event:/aircraft/gui/vws/rita/vws_critical_angle` |  |
| `event:/aircraft/gui/vws/rita/vws_critical_engine_vibration` |  |
| `event:/aircraft/gui/vws/rita/vws_critical_engine_vibration (2)` |  |
| `event:/aircraft/gui/vws/rita/vws_critical_left_engine_vibration` |  |
| `event:/aircraft/gui/vws/rita/vws_critical_right_engine_vibration` |  |
| `event:/aircraft/gui/vws/rita/vws_critical_speed` |  |
| `event:/aircraft/gui/vws/rita/vws_dangerous_close` |  |
| `event:/aircraft/gui/vws/rita/vws_decrease_engine_rpm` |  |
| `event:/aircraft/gui/vws/rita/vws_decrease_left_engine_rpm` |  |
| `event:/aircraft/gui/vws/rita/vws_decrease_right_engine_rpm` |  |
| `event:/aircraft/gui/vws/rita/vws_eject` |  |
| `event:/aircraft/gui/vws/rita/vws_engine_failure` |  |
| `event:/aircraft/gui/vws/rita/vws_engine_fire` |  |
| `event:/aircraft/gui/vws/rita/vws_engine_fire_left` |  |
| `event:/aircraft/gui/vws/rita/vws_engine_fire_right` |  |
| `event:/aircraft/gui/vws/rita/vws_engine_overheat` |  |
| `event:/aircraft/gui/vws/rita/vws_fire` |  |
| `event:/aircraft/gui/vws/rita/vws_fuel_low` |  |
| `event:/aircraft/gui/vws/rita/vws_gear_down` |  |
| `event:/aircraft/gui/vws/rita/vws_generator_failure` |  |
| `event:/aircraft/gui/vws/rita/vws_high` |  |
| `event:/aircraft/gui/vws/rita/vws_hydrosystem_failure` |  |
| `event:/aircraft/gui/vws/rita/vws_increase_engine_rpm` |  |
| `event:/aircraft/gui/vws/rita/vws_jammer` |  |
| `event:/aircraft/gui/vws/rita/vws_jammer_v2` |  |
| `event:/aircraft/gui/vws/rita/vws_left` |  |
| `event:/aircraft/gui/vws/rita/vws_left_engine_failure` |  |
| `event:/aircraft/gui/vws/rita/vws_left_engine_overheat` |  |
| `event:/aircraft/gui/vws/rita/vws_left_generator_failure` |  |
| `event:/aircraft/gui/vws/rita/vws_lock` |  |
| `event:/aircraft/gui/vws/rita/vws_lock_cockpit` |  |
| `event:/aircraft/gui/vws/rita/vws_low` |  |
| `event:/aircraft/gui/vws/rita/vws_main_gearbox_failure` |  |
| `event:/aircraft/gui/vws/rita/vws_missile` |  |
| `event:/aircraft/gui/vws/rita/vws_missile_launch` |  |
| `event:/aircraft/gui/vws/rita/vws_over_g` |  |
| `event:/aircraft/gui/vws/rita/vws_pull_up` |  |
| `event:/aircraft/gui/vws/rita/vws_right` |  |
| `event:/aircraft/gui/vws/rita/vws_right_engine_failure` |  |
| `event:/aircraft/gui/vws/rita/vws_right_engine_overheat` |  |
| `event:/aircraft/gui/vws/rita/vws_right_generator_failure` |  |
| `event:/aircraft/gui/vws/rita/vws_roll_left` |  |
| `event:/aircraft/gui/vws/rita/vws_roll_right` |  |
| `event:/aircraft/gui/vws/rita/vws_tailrotor_gearbox_failure` |  |
| `event:/aircraft/gui/vws/xiao906/vws_ahead` |  |
| `event:/aircraft/gui/vws/xiao906/vws_airbrake` |  |
| `event:/aircraft/gui/vws/xiao906/vws_altitude` |  |
| `event:/aircraft/gui/vws/xiao906/vws_attack_air` |  |
| `event:/aircraft/gui/vws/xiao906/vws_attack_gepard` |  |
| `event:/aircraft/gui/vws/xiao906/vws_attack_sam` |  |
| `event:/aircraft/gui/vws/xiao906/vws_attack_stinger` |  |
| `event:/aircraft/gui/vws/xiao906/vws_behind` |  |
| `event:/aircraft/gui/vws/xiao906/vws_bingo` |  |
| `event:/aircraft/gui/vws/xiao906/vws_caution` |  |
| `event:/aircraft/gui/vws/xiao906/vws_chaff_flare` |  |
| `event:/aircraft/gui/vws/xiao906/vws_check_fuel` |  |
| `event:/aircraft/gui/vws/xiao906/vws_check_gear` |  |
| `event:/aircraft/gui/vws/xiao906/vws_check_mech` |  |
| `event:/aircraft/gui/vws/xiao906/vws_counter` |  |
| `event:/aircraft/gui/vws/xiao906/vws_critical_altitude` |  |
| `event:/aircraft/gui/vws/xiao906/vws_critical_angle` |  |
| `event:/aircraft/gui/vws/xiao906/vws_critical_engine_vibration` |  |
| `event:/aircraft/gui/vws/xiao906/vws_critical_left_engine_vibration` |  |
| `event:/aircraft/gui/vws/xiao906/vws_critical_right_engine_vibration` |  |
| `event:/aircraft/gui/vws/xiao906/vws_critical_speed` |  |
| `event:/aircraft/gui/vws/xiao906/vws_dangerous_close` |  |
| `event:/aircraft/gui/vws/xiao906/vws_dangerous_vibration` |  |
| `event:/aircraft/gui/vws/xiao906/vws_decrease_engine_rpm` |  |
| `event:/aircraft/gui/vws/xiao906/vws_decrease_left_engine_rpm` |  |
| `event:/aircraft/gui/vws/xiao906/vws_decrease_right_engine_rpm` |  |
| `event:/aircraft/gui/vws/xiao906/vws_eject` |  |
| `event:/aircraft/gui/vws/xiao906/vws_engine_failure` |  |
| `event:/aircraft/gui/vws/xiao906/vws_engine_fire` |  |
| `event:/aircraft/gui/vws/xiao906/vws_engine_fire_left` |  |
| `event:/aircraft/gui/vws/xiao906/vws_engine_fire_right` |  |
| `event:/aircraft/gui/vws/xiao906/vws_engine_overheat` |  |
| `event:/aircraft/gui/vws/xiao906/vws_fire` |  |
| `event:/aircraft/gui/vws/xiao906/vws_fuel_low` |  |
| `event:/aircraft/gui/vws/xiao906/vws_gear_down` |  |
| `event:/aircraft/gui/vws/xiao906/vws_generator_failure` |  |
| `event:/aircraft/gui/vws/xiao906/vws_high` |  |
| `event:/aircraft/gui/vws/xiao906/vws_hydrosystem_failure` |  |
| `event:/aircraft/gui/vws/xiao906/vws_increase_engine_rpm` |  |
| `event:/aircraft/gui/vws/xiao906/vws_jammer` |  |
| `event:/aircraft/gui/vws/xiao906/vws_left` |  |
| `event:/aircraft/gui/vws/xiao906/vws_left_engine_failure` |  |
| `event:/aircraft/gui/vws/xiao906/vws_left_engine_overheat` |  |
| `event:/aircraft/gui/vws/xiao906/vws_left_generator_failure` |  |
| `event:/aircraft/gui/vws/xiao906/vws_lock` |  |
| `event:/aircraft/gui/vws/xiao906/vws_lock_cockpit` |  |
| `event:/aircraft/gui/vws/xiao906/vws_low` |  |
| `event:/aircraft/gui/vws/xiao906/vws_main_gearbox_failure` |  |
| `event:/aircraft/gui/vws/xiao906/vws_missile` |  |
| `event:/aircraft/gui/vws/xiao906/vws_missile_launch` |  |
| `event:/aircraft/gui/vws/xiao906/vws_out` |  |
| `event:/aircraft/gui/vws/xiao906/vws_over_g` |  |
| `event:/aircraft/gui/vws/xiao906/vws_pull_up` |  |
| `event:/aircraft/gui/vws/xiao906/vws_right` |  |
| `event:/aircraft/gui/vws/xiao906/vws_right_engine_failure` |  |
| `event:/aircraft/gui/vws/xiao906/vws_right_engine_overheat` |  |
| `event:/aircraft/gui/vws/xiao906/vws_right_generator_failure` |  |
| `event:/aircraft/gui/vws/xiao906/vws_roll_left` |  |
| `event:/aircraft/gui/vws/xiao906/vws_roll_right` |  |
| `event:/aircraft/gui/vws/xiao906/vws_tailrotor_gearbox_failure` |  |
| `event:/aircraft/gui/vws/xiao906/vws_warning` |  |
| `event:/aircraft/gui/wts_mission_complete` |  |
| `event:/aircraft/gui/wts_mission_failed` |  |
| `event:/aircraft/gui/ww_airfield_select` |  |
| `event:/aircraft/gui/ww_airfield_send` |  |
| `event:/aircraft/gui/ww_artillery_enemy` |  |
| `event:/aircraft/gui/ww_artillery_player` |  |
| `event:/aircraft/gui/ww_battle_end_fail` |  |
| `event:/aircraft/gui/ww_battle_end_win` |  |
| `event:/aircraft/gui/ww_battle_start` |  |
| `event:/aircraft/gui/ww_enemy_airplane_incoming` |  |
| `event:/aircraft/gui/ww_enemy_reinf_airplanes` |  |
| `event:/aircraft/gui/ww_enemy_reinf_artillery` |  |
| `event:/aircraft/gui/ww_enemy_reinf_infantry` |  |
| `event:/aircraft/gui/ww_enemy_reinf_tanks` |  |
| `event:/aircraft/gui/ww_globe_battle_select` |  |
| `event:/aircraft/gui/ww_oper_end_fail` |  |
| `event:/aircraft/gui/ww_oper_end_win` |  |
| `event:/aircraft/gui/ww_reinforcement_select` |  |
| `event:/aircraft/gui/ww_unit_entrench` |  |
| `event:/aircraft/gui/ww_unit_entrench_move_notify` |  |
| `event:/aircraft/gui/ww_unit_move` |  |
| `event:/aircraft/gui/ww_unit_move_airplanes` |  |
| `event:/aircraft/gui/ww_unit_move_artillery` |  |
| `event:/aircraft/gui/ww_unit_move_helicopters` |  |
| `event:/aircraft/gui/ww_unit_move_infantry` |  |
| `event:/aircraft/gui/ww_unit_move_tanks` |  |
| `event:/aircraft/gui/ww_unit_select` |  |

## aircraft_guns

374 events (270 named), 3162 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/aircraft/weapon/a127_gun_ai` | Distance, alternative_rpm, Direction, on_shot, guns, headphones |
| `event:/aircraft/weapon/a127_gun_inside` | guns, on_shot, alternative_rpm |
| `event:/aircraft/weapon/a127_gun_outside` | alternative_rpm, on_shot, listener_altitude, Distance, Event Cone Angle, guns |
| `event:/aircraft/weapon/aa12mm_fire_ai` | Direction, on_shot, Distance, guns, headphones |
| `event:/aircraft/weapon/aa37mm_fire_ai` | Direction, on_shot, Distance, Event Cone Angle, headphones |
| `event:/aircraft/weapon/aa_big_gun_fire_ai` | Direction, on_shot, Distance, Event Cone Angle, headphones |
| `event:/aircraft/weapon/aa_big_mg_fire_ai` | Direction, Distance, on_shot, guns, headphones |
| `event:/aircraft/weapon/aa_gun_explosion_s` | Distance |
| `event:/aircraft/weapon/aa_gun_fire_ai` | Event Cone Angle, headphones, on_shot, Direction, Distance |
| `event:/aircraft/weapon/aa_medium_gun_fire_ai` | headphones, Event Cone Angle, Distance, on_shot, Direction |
| `event:/aircraft/weapon/aa_medium_mg_fire_ai` | on_shot, Distance, Direction, headphones, guns |
| `event:/aircraft/weapon/aa_small_gun_fire_ai` | Distance, Direction, on_shot, headphones, Event Cone Angle |
| `event:/aircraft/weapon/aa_small_mg_fire_ai` | Distance, on_shot, Direction, headphones, guns |
| `event:/aircraft/weapon/bereda-safat_127_gun_ai` | guns, headphones, Distance, on_shot, Direction |
| `event:/aircraft/weapon/bereda-safat_127_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/bereda-safat_127_gun_outside` | Event Cone Angle, Distance, guns, listener_altitude, on_shot |
| `event:/aircraft/weapon/bereda-safat_77_gun_ai` | Distance, on_shot, Direction, guns, headphones |
| `event:/aircraft/weapon/bereda-safat_77_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/bereda-safat_77_gun_outside` | listener_altitude, on_shot, Event Cone Angle, Distance, guns |
| `event:/aircraft/weapon/berezin_gun_ai` | headphones, guns, on_shot, Direction, Distance |
| `event:/aircraft/weapon/berezin_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/berezin_gun_outside` | on_shot, listener_altitude, Distance, Event Cone Angle, guns |
| `event:/aircraft/weapon/bk37_gun_ai` | on_shot, Event Cone Angle, Distance, Direction, headphones |
| `event:/aircraft/weapon/bk37_gun_inside` | on_shot, alternative_rpm, breechInCockpit, guns, Distance |
| `event:/aircraft/weapon/bk37_gun_outside` | Event Cone Angle, on_shot, alternative_rpm, Distance, listener_altitude, guns, onGround, zoom |
| `event:/aircraft/weapon/bk75_gun_ai` | Direction, Event Cone Angle, Distance, on_shot, headphones |
| `event:/aircraft/weapon/bk75_gun_inside` | guns, Distance, on_shot, alternative_rpm, breechInCockpit |
| `event:/aircraft/weapon/bk75_gun_outside` | listener_altitude, Event Cone Angle, Distance, alternative_rpm, on_shot, onGround, zoom, guns |
| `event:/aircraft/weapon/cannon_2A42_ai` | guns, headphones, Distance, alternative_rpm, Direction, on_shot |
| `event:/aircraft/weapon/cannon_2A42_inside` | guns, on_shot, alternative_rpm |
| `event:/aircraft/weapon/cannon_2A42_outside` | on_shot, listener_altitude, alternative_rpm, Distance, Event Cone Angle, guns |
| `event:/aircraft/weapon/cannon_M230E1_ai` | alternative_rpm, Distance, Direction, on_shot, guns, headphones |
| `event:/aircraft/weapon/cannon_M230E1_inside` | guns, on_shot, alternative_rpm |
| `event:/aircraft/weapon/cannon_M230E1_outside` | alternative_rpm, listener_altitude, on_shot, guns, Event Cone Angle, Distance |
| `event:/aircraft/weapon/cannon_aden_ai` | headphones, guns, on_shot, Direction, Distance |
| `event:/aircraft/weapon/cannon_aden_inside` | guns, on_shot |
| `event:/aircraft/weapon/cannon_aden_outside` | guns, Event Cone Angle, Distance, listener_altitude, on_shot |
| `event:/aircraft/weapon/cannon_giat_m791_ai` | headphones, guns, on_shot, Direction, Distance |
| `event:/aircraft/weapon/cannon_giat_m791_inside` | on_shot, guns |
| `event:/aircraft/weapon/cannon_giat_m791_outside` | listener_altitude, on_shot, Event Cone Angle, Distance, guns |
| `event:/aircraft/weapon/cannon_giat_type_30_M780_ai` | Direction, on_shot, Distance, headphones, guns |
| `event:/aircraft/weapon/cannon_giat_type_30_M780_inside` | guns, on_shot |
| `event:/aircraft/weapon/cannon_giat_type_30_M780_outside` | on_shot, listener_altitude, Distance, Event Cone Angle, guns |
| `event:/aircraft/weapon/cannon_gsh_23_ai` | Direction, on_shot, Distance, headphones, guns |
| `event:/aircraft/weapon/cannon_gsh_23_inside` | guns, on_shot |
| `event:/aircraft/weapon/cannon_gsh_23_outside` | listener_altitude, on_shot, guns, Event Cone Angle, Distance |
| `event:/aircraft/weapon/cannon_gsh_23l_ai` | Distance, Direction, on_shot, guns, headphones |
| `event:/aircraft/weapon/cannon_gsh_23l_inside` | guns, on_shot |
| `event:/aircraft/weapon/cannon_gsh_23l_outside` | Event Cone Angle, Distance, guns, listener_altitude, on_shot |
| `event:/aircraft/weapon/cannon_gsh_30_2_ai` | Distance, alternative_rpm, Direction, on_shot, guns, headphones |
| `event:/aircraft/weapon/cannon_gsh_30_2_inside` | alternative_rpm, on_shot, guns |
| `event:/aircraft/weapon/cannon_gsh_30_2_outside` | alternative_rpm, on_shot, listener_altitude, guns, Distance, Event Cone Angle |
| `event:/aircraft/weapon/cannon_nr_30_ai` | Distance, on_shot, Direction, guns, headphones |
| `event:/aircraft/weapon/cannon_nr_30_inside` | guns, on_shot |
| `event:/aircraft/weapon/cannon_nr_30_outside` | Event Cone Angle, Distance, guns, listener_altitude, on_shot |
| `event:/aircraft/weapon/cannon_t_160_ai` | headphones, guns, Direction, on_shot, Distance |
| `event:/aircraft/weapon/cannon_t_160_inside` | on_shot, guns |
| `event:/aircraft/weapon/cannon_t_160_outside` | listener_altitude, on_shot, guns, Event Cone Angle, Distance |
| `event:/aircraft/weapon/cannon_type_23l_ai` | guns, headphones, Distance, alternative_rpm, on_shot, Direction |
| `event:/aircraft/weapon/cannon_type_23l_inside` | on_shot, alternative_rpm, guns |
| `event:/aircraft/weapon/cannon_type_23l_outside` | alternative_rpm, on_shot, listener_altitude, Distance, Event Cone Angle, guns |
| `event:/aircraft/weapon/cannon_xm140_ai` | Direction, on_shot, Distance, headphones, guns |
| `event:/aircraft/weapon/cannon_xm140_inside` | on_shot, guns |
| `event:/aircraft/weapon/cannon_xm140_outside` | on_shot, listener_altitude, guns, Distance, Event Cone Angle |
| `event:/aircraft/weapon/chaff_launcher_inside` | Distance, on_shot |
| `event:/aircraft/weapon/chaff_launcher_outside` | listener_altitude, on_shot, Distance, Event Cone Angle, onGround |
| `event:/aircraft/weapon/chaff_launcher_outside_ai` | headphones, Distance, Direction, listener_altitude, on_shot |
| `event:/aircraft/weapon/degtyaryov_gun_ai` | Distance, Direction, on_shot, guns, headphones |
| `event:/aircraft/weapon/degtyaryov_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/degtyaryov_gun_outside` | on_shot, listener_altitude, guns, Distance, Event Cone Angle |
| `event:/aircraft/weapon/flare_launcher_inside` | on_shot, Distance |
| `event:/aircraft/weapon/flare_launcher_outside` | listener_altitude, Distance, on_shot, Event Cone Angle, onGround |
| `event:/aircraft/weapon/flare_launcher_outside_ai` | headphones, Distance, listener_altitude, Direction, on_shot |
| `event:/aircraft/weapon/gau_12_gun_ai` | guns, headphones, Distance, on_shot, Direction |
| `event:/aircraft/weapon/gau_12_gun_inside` | on_shot, Distance, guns |
| `event:/aircraft/weapon/gau_12_gun_outside` | Distance, Event Cone Angle, guns, onGround, on_shot, listener_altitude |
| `event:/aircraft/weapon/gau_12_gun_rotor` | on_shot, alternative_rpm, Distance |
| `event:/aircraft/weapon/gau_12_gun_rotor_interior` | on_shot, alternative_rpm |
| `event:/aircraft/weapon/gau_13a_gun_ai` | Distance, on_shot, Direction, guns, headphones |
| `event:/aircraft/weapon/gau_13a_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/gau_13a_gun_outside` | guns, Event Cone Angle, Distance, listener_altitude, on_shot |
| `event:/aircraft/weapon/gau_13a_gun_rotor` | Distance, alternative_rpm, on_shot |
| `event:/aircraft/weapon/gau_13a_gun_rotor_interior` | on_shot, alternative_rpm |
| `event:/aircraft/weapon/gau_19_ai` | headphones, guns, on_shot, listener_altitude, Direction, Distance |
| `event:/aircraft/weapon/gau_19_inside` | on_shot, Distance, guns |
| `event:/aircraft/weapon/gau_19_outside` | listener_altitude, on_shot, guns, Event Cone Angle, Distance |
| `event:/aircraft/weapon/gau_19_rotor_inside` | alternative_rpm, on_shot |
| `event:/aircraft/weapon/gau_19_rotor_outside` | Distance, alternative_rpm, on_shot |
| `event:/aircraft/weapon/gau_8a_gun_ai` | headphones, guns, on_shot, Direction, listener_altitude, Distance |
| `event:/aircraft/weapon/gau_8a_gun_inside` | Distance, guns, on_shot |
| `event:/aircraft/weapon/gau_8a_gun_outside` | listener_altitude, on_shot, onGround, guns, Event Cone Angle, Distance |
| `event:/aircraft/weapon/gau_8a_gun_rotor` | Distance, alternative_rpm, on_shot |
| `event:/aircraft/weapon/gau_8a_gun_rotor_interior` | alternative_rpm, on_shot |
| `event:/aircraft/weapon/gsh_30_1_ai` | guns, headphones, Distance, listener_altitude, Direction, on_shot |
| `event:/aircraft/weapon/gsh_30_1_inside` | on_shot, guns, Distance |
| `event:/aircraft/weapon/gsh_30_1_outside` | Event Cone Angle, Distance, guns, listener_altitude, on_shot |
| `event:/aircraft/weapon/gsh_6_23_ai` | headphones, guns, Direction, on_shot, Distance |
| `event:/aircraft/weapon/gsh_6_23_inside` | guns, on_shot |
| `event:/aircraft/weapon/gsh_6_23_outside` | onGround, guns, Event Cone Angle, Distance, listener_altitude, on_shot |
| `event:/aircraft/weapon/gsh_6_23_rotor` | on_shot, alternative_rpm, Distance |
| `event:/aircraft/weapon/gsh_6_23_rotor_interior` | alternative_rpm, on_shot |
| `event:/aircraft/weapon/gsh_6_30_gun_ai` | on_shot, Direction, Distance, headphones, guns |
| `event:/aircraft/weapon/gsh_6_30_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/gsh_6_30_gun_outside` | on_shot, listener_altitude, Distance, Event Cone Angle, guns |
| `event:/aircraft/weapon/gsh_6_30_gun_rotor` | Distance, on_shot, alternative_rpm |
| `event:/aircraft/weapon/gsh_6_30_gun_rotor_interior` | alternative_rpm, on_shot |
| `event:/aircraft/weapon/gshg_gun_ai` | Distance, Direction, listener_altitude, on_shot, guns, headphones |
| `event:/aircraft/weapon/gshg_gun_inside` | Distance, guns, on_shot |
| `event:/aircraft/weapon/gshg_gun_outside` | guns, Distance, Event Cone Angle, on_shot, listener_altitude |
| `event:/aircraft/weapon/gshg_gun_rotor_inside` | alternative_rpm, on_shot |
| `event:/aircraft/weapon/gshg_gun_rotor_outside` | Distance, alternative_rpm, on_shot |
| `event:/aircraft/weapon/ho204_gun_ai` | headphones, guns, Direction, on_shot, Distance |
| `event:/aircraft/weapon/ho204_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/ho204_gun_outside` | Distance, Event Cone Angle, guns, on_shot, listener_altitude |
| `event:/aircraft/weapon/ho301_gun_ai` | Distance, on_shot, Direction, guns, headphones |
| `event:/aircraft/weapon/ho301_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/ho301_gun_outside` | guns, Distance, Event Cone Angle, on_shot, listener_altitude |
| `event:/aircraft/weapon/hs404_gun_ai` | guns, headphones, Distance, Direction, on_shot |
| `event:/aircraft/weapon/hs404_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/hs404_gun_outside` | listener_altitude, on_shot, guns, Event Cone Angle, Distance |
| `event:/aircraft/weapon/hs_mk2_gun_ai` | Direction, on_shot, Distance, headphones, guns |
| `event:/aircraft/weapon/hs_mk2_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/hs_mk2_gun_outside` | guns, Event Cone Angle, Distance, listener_altitude, on_shot |
| `event:/aircraft/weapon/hs_mk5_gun_ai` | guns, headphones, Distance, Direction, on_shot |
| `event:/aircraft/weapon/hs_mk5_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/hs_mk5_gun_outside` | listener_altitude, on_shot, guns, Event Cone Angle, Distance |
| `event:/aircraft/weapon/kord_gun_ai` | Distance, on_shot, Direction, guns, headphones |
| `event:/aircraft/weapon/kord_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/kord_gun_outside` | on_shot, listener_altitude, Distance, Event Cone Angle, guns |
| `event:/aircraft/weapon/m129_launcher_ai` | Distance, on_shot, Direction, guns, headphones |
| `event:/aircraft/weapon/m129_launcher_inside` | on_shot, guns |
| `event:/aircraft/weapon/m129_launcher_outside` | guns, Event Cone Angle, Distance, listener_altitude, on_shot |
| `event:/aircraft/weapon/m134_gun_ai` | headphones, guns, alternative_rpm, Direction, on_shot, Distance |
| `event:/aircraft/weapon/m134_gun_inside` | guns, alternative_rpm, on_shot |
| `event:/aircraft/weapon/m134_gun_outside` | Distance, Event Cone Angle, guns, on_shot, listener_altitude, alternative_rpm |
| `event:/aircraft/weapon/m134_rotor_inside` | alternative_rpm, on_shot |
| `event:/aircraft/weapon/m134_rotor_outside` | listener_altitude, Distance |
| `event:/aircraft/weapon/m1919_gun_ai` | guns, headphones, Distance, Direction, on_shot |
| `event:/aircraft/weapon/m1919_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/m1919_gun_outside` | listener_altitude, on_shot, guns, Event Cone Angle, Distance |
| `event:/aircraft/weapon/m1919_high_rate_gun_ai` | Direction, on_shot, Distance, headphones, guns |
| `event:/aircraft/weapon/m1919_high_rate_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/m1919_high_rate_gun_outside` | Event Cone Angle, Distance, guns, listener_altitude, on_shot |
| `event:/aircraft/weapon/m197_gun_ai` | guns, headphones, Distance, Direction, on_shot |
| `event:/aircraft/weapon/m197_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/m197_gun_outside` | Event Cone Angle, Distance, guns, listener_altitude, on_shot |
| `event:/aircraft/weapon/m197_rotor_inside` | on_shot, alternative_rpm |
| `event:/aircraft/weapon/m197_rotor_outside` | Distance, alternative_rpm, on_shot, listener_altitude |
| `event:/aircraft/weapon/m2_gun_ai` | headphones, guns, Direction, on_shot, Distance |
| `event:/aircraft/weapon/m2_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/m2_gun_outside` | listener_altitude, on_shot, Event Cone Angle, Distance, guns |
| `event:/aircraft/weapon/m3_gun_ai` | guns, headphones, Distance, on_shot, Direction |
| `event:/aircraft/weapon/m3_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/m3_gun_outside` | guns, Distance, Event Cone Angle, on_shot, listener_altitude |
| `event:/aircraft/weapon/m4_75_gun_ai` | Event Cone Angle, Distance, on_shot, Direction, headphones |
| `event:/aircraft/weapon/m4_75_gun_inside` | guns, Distance, breechInCockpit, alternative_rpm, on_shot |
| `event:/aircraft/weapon/m4_75_gun_outside` | listener_altitude, Event Cone Angle, alternative_rpm, on_shot, Distance, onGround, zoom, guns |
| `event:/aircraft/weapon/m4_gun_ai` | Direction, on_shot, Event Cone Angle, Distance, headphones |
| `event:/aircraft/weapon/m4_gun_inside` | alternative_rpm, on_shot, breechInCockpit, guns, Distance |
| `event:/aircraft/weapon/m4_gun_outside` | onGround, zoom, Event Cone Angle, guns, listener_altitude, Distance, alternative_rpm, on_shot |
| `event:/aircraft/weapon/m5_gun_ai` | Distance, headphones, on_shot, Event Cone Angle, Direction |
| `event:/aircraft/weapon/m5_gun_inside` | on_shot, alternative_rpm, breechInCockpit, guns, Distance |
| `event:/aircraft/weapon/m5_gun_outside` | onGround, zoom, Event Cone Angle, guns, listener_altitude, Distance, on_shot, alternative_rpm |
| `event:/aircraft/weapon/m61_gun_ai` | headphones, guns, Direction, on_shot, Distance |
| `event:/aircraft/weapon/m61_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/m61_gun_outside` | onGround, Event Cone Angle, Distance, guns, listener_altitude, on_shot |
| `event:/aircraft/weapon/m61_gun_rotor` | alternative_rpm, on_shot, Distance |
| `event:/aircraft/weapon/m61_gun_rotor_interior` | on_shot, alternative_rpm |
| `event:/aircraft/weapon/mauser_27mm_ai` | Distance, listener_altitude, Direction, on_shot, guns, headphones |
| `event:/aircraft/weapon/mauser_27mm_inside` | on_shot, Distance, guns |
| `event:/aircraft/weapon/mauser_27mm_outside` | on_shot, listener_altitude, Distance, Event Cone Angle, guns |
| `event:/aircraft/weapon/mg151_gun_ai` | Direction, on_shot, Distance, headphones, guns |
| `event:/aircraft/weapon/mg151_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/mg151_gun_outside` | listener_altitude, on_shot, Event Cone Angle, Distance, guns |
| `event:/aircraft/weapon/mg15_gun_ai` | headphones, guns, Direction, on_shot, Distance |
| `event:/aircraft/weapon/mg15_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/mg15_gun_outside` | listener_altitude, on_shot, Event Cone Angle, Distance, guns |
| `event:/aircraft/weapon/mg17_gun_ai` | Direction, on_shot, Distance, headphones, guns |
| `event:/aircraft/weapon/mg17_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/mg17_gun_outside` | listener_altitude, on_shot, Event Cone Angle, Distance, guns |
| `event:/aircraft/weapon/mg81_gun_ai` | headphones, guns, Direction, on_shot, Distance |
| `event:/aircraft/weapon/mg81_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/mg81_gun_outside` | guns, Distance, Event Cone Angle, on_shot, listener_altitude |
| `event:/aircraft/weapon/mg_131_gun_ai` | guns, headphones, Distance, on_shot, Direction |
| `event:/aircraft/weapon/mg_131_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/mg_131_gun_outside` | listener_altitude, on_shot, Event Cone Angle, Distance, guns |
| `event:/aircraft/weapon/mgc30l_gun_ai` | Distance, Direction, on_shot, guns, headphones |
| `event:/aircraft/weapon/mgc30l_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/mgc30l_gun_outside` | Event Cone Angle, Distance, guns, listener_altitude, on_shot |
| `event:/aircraft/weapon/mgff_gun_ai` | Distance, Direction, on_shot, guns, headphones |
| `event:/aircraft/weapon/mgff_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/mgff_gun_outside` | on_shot, listener_altitude, guns, Distance, Event Cone Angle |
| `event:/aircraft/weapon/missile_heavy_fly` | headphones, Event Cone Angle, Elevation, Distance, Direction, mach, thrust |
| `event:/aircraft/weapon/missile_heavy_inside_start` | on_shot, Distance, Event Cone Angle, onGround |
| `event:/aircraft/weapon/missile_heavy_start` | Distance, on_shot, onGround, Event Cone Angle |
| `event:/aircraft/weapon/missile_heavy_start_ai` | Direction, on_shot, Distance, headphones |
| `event:/aircraft/weapon/missile_light_fly` | Direction, thrust, mach, headphones, Distance, Event Cone Angle, Elevation |
| `event:/aircraft/weapon/missile_light_inside_start` | on_shot, Distance, onGround, Event Cone Angle |
| `event:/aircraft/weapon/missile_light_start` | Event Cone Angle, onGround, Distance, on_shot |
| `event:/aircraft/weapon/missile_light_start_ai` | headphones, Distance, Direction, on_shot |
| `event:/aircraft/weapon/missile_med_fly` | mach, thrust, Direction, Distance, Event Cone Angle, Elevation, headphones |
| `event:/aircraft/weapon/missile_med_inside_start` | Distance, on_shot, Event Cone Angle, onGround |
| `event:/aircraft/weapon/missile_med_start` | Distance, on_shot, Event Cone Angle, onGround |
| `event:/aircraft/weapon/missile_med_start_ai` | on_shot, Distance, Direction, headphones |
| `event:/aircraft/weapon/mk_103_38_gun_ai` | headphones, guns, on_shot, Direction, Distance |
| `event:/aircraft/weapon/mk_103_38_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/mk_103_38_gun_outside` | on_shot, listener_altitude, Distance, Event Cone Angle, guns |
| `event:/aircraft/weapon/mk_103_gun_ai` | on_shot, Direction, Distance, headphones, guns |
| `event:/aircraft/weapon/mk_103_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/mk_103_gun_outside` | on_shot, listener_altitude, guns, Distance, Event Cone Angle |
| `event:/aircraft/weapon/mk_108_gun_ai` | headphones, guns, on_shot, Direction, Distance |
| `event:/aircraft/weapon/mk_108_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/mk_108_gun_outside` | listener_altitude, on_shot, Event Cone Angle, Distance, guns |
| `event:/aircraft/weapon/mollins57_gun_ai` | Distance, headphones, Event Cone Angle, on_shot, Direction |
| `event:/aircraft/weapon/mollins57_gun_inside` | alternative_rpm, on_shot, breechInCockpit, guns, Distance |
| `event:/aircraft/weapon/mollins57_gun_outside` | listener_altitude, on_shot, alternative_rpm, Distance, Event Cone Angle, zoom, onGround, guns |
| `event:/aircraft/weapon/npc_rifle_fire` | Distance, Direction, on_shot, headphones |
| `event:/aircraft/weapon/nr23_gun_ai` | on_shot, Direction, Distance, headphones, guns |
| `event:/aircraft/weapon/nr23_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/nr23_gun_outside` | guns, Distance, Event Cone Angle, on_shot, listener_altitude |
| `event:/aircraft/weapon/ns37_gun_ai` | on_shot, Event Cone Angle, Distance, Direction, headphones |
| `event:/aircraft/weapon/ns37_gun_inside` | alternative_rpm, on_shot, breechInCockpit, Distance, guns |
| `event:/aircraft/weapon/ns37_gun_outside` | listener_altitude, Event Cone Angle, Distance, on_shot, alternative_rpm, onGround, zoom, guns |
| `event:/aircraft/weapon/ns45_gun_ai` | Direction, Distance, Event Cone Angle, on_shot, headphones |
| `event:/aircraft/weapon/ns45_gun_inside` | guns, Distance, breechInCockpit, on_shot, alternative_rpm |
| `event:/aircraft/weapon/ns45_gun_outside` | zoom, onGround, guns, Event Cone Angle, listener_altitude, alternative_rpm, on_shot, Distance |
| `event:/aircraft/weapon/rocket_fly` | Event Cone Angle, Distance |
| `event:/aircraft/weapon/rocket_start` | Event Cone Angle, onGround, on_shot, Distance |
| `event:/aircraft/weapon/rocket_start_ai` | Distance, headphones, on_shot, Direction |
| `event:/aircraft/weapon/shkasi_gun_ai` | Direction, on_shot, Distance, headphones, guns |
| `event:/aircraft/weapon/shkasi_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/shkasi_gun_outside` | guns, Distance, Event Cone Angle, on_shot, listener_altitude |
| `event:/aircraft/weapon/shvak_gun_ai` | Direction, on_shot, Distance, headphones, guns |
| `event:/aircraft/weapon/shvak_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/shvak_gun_outside` | on_shot, listener_altitude, Distance, Event Cone Angle, guns |
| `event:/aircraft/weapon/type3_gun_ai` | Direction, on_shot, Distance, headphones, guns |
| `event:/aircraft/weapon/type3_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/type3_gun_outside` | Event Cone Angle, Distance, guns, listener_altitude, on_shot |
| `event:/aircraft/weapon/type88_gun_ai` | headphones, Distance, Direction, on_shot, Event Cone Angle |
| `event:/aircraft/weapon/type88_gun_inside` | alternative_rpm, on_shot, breechInCockpit, Distance, guns |
| `event:/aircraft/weapon/type88_gun_outside` | onGround, zoom, Event Cone Angle, guns, listener_altitude, Distance, on_shot, alternative_rpm |
| `event:/aircraft/weapon/type92_gun_ai` | on_shot, Direction, Distance, headphones, guns |
| `event:/aircraft/weapon/type92_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/type92_gun_outside` | on_shot, listener_altitude, Distance, Event Cone Angle, guns |
| `event:/aircraft/weapon/type97_gun_ai` | guns, headphones, Distance, on_shot, Direction |
| `event:/aircraft/weapon/type97_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/type97_gun_outside` | listener_altitude, on_shot, Event Cone Angle, Distance, guns |
| `event:/aircraft/weapon/type99_gun_ai` | headphones, guns, Direction, on_shot, Distance |
| `event:/aircraft/weapon/type99_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/type99_gun_outside` | guns, Event Cone Angle, Distance, listener_altitude, on_shot |
| `event:/aircraft/weapon/vickers_k_gun_ai` | Direction, on_shot, Distance, headphones, guns |
| `event:/aircraft/weapon/vickers_k_gun_inside` | on_shot, guns |
| `event:/aircraft/weapon/vickers_k_gun_outside` | Event Cone Angle, Distance, guns, listener_altitude, on_shot |
| `event:/aircraft/weapon/vickers_s_gun_ai` | Direction, on_shot, Distance, Event Cone Angle, headphones |
| `event:/aircraft/weapon/vickers_s_gun_inside` | alternative_rpm, on_shot, breechInCockpit, Distance, guns |
| `event:/aircraft/weapon/vickers_s_gun_outside` | listener_altitude, on_shot, alternative_rpm, Distance, Event Cone Angle, zoom, onGround, guns |
| `event:/aircraft/weapon/vya23_gun_ai` | headphones, guns, Direction, on_shot, Distance |
| `event:/aircraft/weapon/vya23_gun_inside` | guns, on_shot |
| `event:/aircraft/weapon/vya23_gun_outside` | listener_altitude, on_shot, Event Cone Angle, Distance, guns |
| `event:/aircraft/weapon/vya23_gun_outside_ai` | headphones, guns, Direction, on_shot, Distance |
| `event:/aircraft/weapon/xm301_gun_ai` | on_shot, Direction, alternative_rpm, Distance, headphones, guns |
| `event:/aircraft/weapon/xm301_gun_inside` | guns, on_shot, alternative_rpm |
| `event:/aircraft/weapon/xm301_gun_outside` | Event Cone Angle, Distance, guns, onGround, alternative_rpm, listener_altitude, on_shot |
| `event:/aircraft/weapon/xm301_gun_rotor` | Distance, alternative_rpm, on_shot |
| `event:/aircraft/weapon/xm301_gun_rotor_interior` | alternative_rpm, on_shot |
| `event:/aircraft/weapon/yak_b_gun_ai` | Distance, Direction, on_shot, alternative_rpm, guns, headphones |
| `event:/aircraft/weapon/yak_b_gun_inside` | on_shot, alternative_rpm, guns |
| `event:/aircraft/weapon/yak_b_gun_outside` | Distance, Event Cone Angle, guns, on_shot, listener_altitude, alternative_rpm |
| `event:/aircraft/weapon/yak_b_rotor_inside` | alternative_rpm, on_shot |
| `event:/aircraft/weapon/yak_b_rotor_outside` | alternative_rpm, on_shot, listener_altitude, Distance |

## aircraft_music

88 events (88 named), 97 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/aircraft/music/1_japan_midway` |  |
| `event:/aircraft/music/1_japan_pearl_harbor` |  |
| `event:/aircraft/music/1_japan_wake` |  |
| `event:/aircraft/music/1_us_coral` |  |
| `event:/aircraft/music/1_us_guadalcanal` |  |
| `event:/aircraft/music/2_japan_coral` |  |
| `event:/aircraft/music/2_japan_guadalcanal` |  |
| `event:/aircraft/music/2_japan_pearl_harbor` |  |
| `event:/aircraft/music/2_us_midway` |  |
| `event:/aircraft/music/2_us_wake` |  |
| `event:/aircraft/music/3_japan_coral` |  |
| `event:/aircraft/music/3_japan_midway_long` |  |
| `event:/aircraft/music/3_us_guadalcanal` |  |
| `event:/aircraft/music/3_us_pearl_harbor` |  |
| `event:/aircraft/music/3_us_wake` |  |
| `event:/aircraft/music/4_us_guadalcanal` |  |
| `event:/aircraft/music/4_us_midway` |  |
| `event:/aircraft/music/4_us_wake_long` |  |
| `event:/aircraft/music/5_japan_guadalcanal` |  |
| `event:/aircraft/music/5_japan_midway_long` |  |
| `event:/aircraft/music/6_us_guadalcanal` |  |
| `event:/aircraft/music/action_01` |  |
| `event:/aircraft/music/action_cs` |  |
| `event:/aircraft/music/australia_defeat_theme` |  |
| `event:/aircraft/music/australia_main_theme` |  |
| `event:/aircraft/music/australia_victory_theme` |  |
| `event:/aircraft/music/benchmark_music` |  |
| `event:/aircraft/music/big_combat_1` |  |
| `event:/aircraft/music/big_combat_2` |  |
| `event:/aircraft/music/big_combat_3` |  |
| `event:/aircraft/music/britain_defeat_theme` |  |
| `event:/aircraft/music/britain_defeat_theme_old` |  |
| `event:/aircraft/music/britain_main_theme` |  |
| `event:/aircraft/music/britain_main_theme_old` |  |
| `event:/aircraft/music/britain_victory_theme` |  |
| `event:/aircraft/music/britain_victory_theme_old` |  |
| `event:/aircraft/music/china_defeat_theme` |  |
| `event:/aircraft/music/china_main_theme` |  |
| `event:/aircraft/music/china_victory_theme` |  |
| `event:/aircraft/music/finland_defeat_theme` |  |
| `event:/aircraft/music/finland_main_theme` |  |
| `event:/aircraft/music/finland_victory_theme` |  |
| `event:/aircraft/music/france_defeat_theme` |  |
| `event:/aircraft/music/france_main_theme` |  |
| `event:/aircraft/music/france_victory_theme` |  |
| `event:/aircraft/music/germany_defeat_theme` |  |
| `event:/aircraft/music/germany_main_theme` |  |
| `event:/aircraft/music/germany_victory_theme` |  |
| `event:/aircraft/music/halloween_2021` |  |
| `event:/aircraft/music/hungary_defeat_theme` |  |
| `event:/aircraft/music/hungary_main_theme` |  |
| `event:/aircraft/music/hungary_victory_theme` |  |
| `event:/aircraft/music/israel_defeat_theme` |  |
| `event:/aircraft/music/israel_main_theme` |  |
| `event:/aircraft/music/israel_victory_theme` |  |
| `event:/aircraft/music/italy_defeat_theme` |  |
| `event:/aircraft/music/italy_main_theme` |  |
| `event:/aircraft/music/italy_victory_theme` |  |
| `event:/aircraft/music/japan_defeat_theme` |  |
| `event:/aircraft/music/japan_main_theme` |  |
| `event:/aircraft/music/japan_victory_theme` |  |
| `event:/aircraft/music/loose` |  |
| `event:/aircraft/music/menu` |  |
| `event:/aircraft/music/new_year` |  |
| `event:/aircraft/music/ships_action_01` |  |
| `event:/aircraft/music/ships_suspense_01` |  |
| `event:/aircraft/music/south_africa_defeat_theme` |  |
| `event:/aircraft/music/south_africa_main_theme` |  |
| `event:/aircraft/music/south_africa_victory_theme` |  |
| `event:/aircraft/music/space_battle_defeat_theme` |  |
| `event:/aircraft/music/space_battle_theme` |  |
| `event:/aircraft/music/space_battle_victory_theme` |  |
| `event:/aircraft/music/suspense_01` |  |
| `event:/aircraft/music/suspense_cs` |  |
| `event:/aircraft/music/sweden_defeat_theme` |  |
| `event:/aircraft/music/sweden_main_theme` |  |
| `event:/aircraft/music/sweden_victory_theme` |  |
| `event:/aircraft/music/tanks_action_01` |  |
| `event:/aircraft/music/tanks_suspense_01` |  |
| `event:/aircraft/music/tension_cs` |  |
| `event:/aircraft/music/usa_defeat_theme` |  |
| `event:/aircraft/music/usa_main_theme` |  |
| `event:/aircraft/music/usa_victory_theme` |  |
| `event:/aircraft/music/ussr_defeat_theme` |  |
| `event:/aircraft/music/ussr_main_theme` |  |
| `event:/aircraft/music/ussr_victory_theme` |  |
| `event:/aircraft/music/valkyries` |  |
| `event:/aircraft/music/win` |  |

## aircraft_music_2

4 events (4 named), 13 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/aircraft/music/chinese_new_year` |  |
| `event:/aircraft/music/menu_birthday` |  |
| `event:/aircraft/music/menu_new` |  |
| `event:/aircraft/music/top_tier/aircraft_action` |  |

## aircraft_music_3

7 events (7 named), 15 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/aircraft/music/belgium_defeat_theme` |  |
| `event:/aircraft/music/belgium_main_theme` |  |
| `event:/aircraft/music/belgium_victory_theme` |  |
| `event:/aircraft/music/thailand_defeat_theme` |  |
| `event:/aircraft/music/thailand_main_theme` |  |
| `event:/aircraft/music/thailand_victory_theme` |  |
| `event:/aircraft/music/top_tier/tank_action` |  |

## aircraft_music_4

4 events (4 named), 12 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/aircraft/music/infantry_action` |  |
| `event:/aircraft/music/infantry_suspense` |  |
| `event:/aircraft/music/jet_dogfight` |  |
| `event:/aircraft/music/menu_infantry` |  |
