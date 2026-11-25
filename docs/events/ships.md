[← Events Index](../EVENTS.md) · [← Docs](../README.md)

# Ships & Naval — sound events

Naval engines, wakes, effects and shipboard weapons. **5 populated bank(s)** · **228 named events**.

| Bank | Named events | Waveforms |
| --- | ---: | ---: |
| [`ships_ambient`](#ships_ambient) | 1 | 20 |
| [`ships_effects`](#ships_effects) | 44 | 250 |
| [`ships_engines`](#ships_engines) | 38 | 92 |
| [`ships_explosions`](#ships_explosions) | 22 | 141 |
| [`ships_weapon`](#ships_weapon) | 123 | 1202 |

## ships_ambient

1 events (1 named), 20 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/naval/ambient/underwater` | action, depth |

## ships_effects

47 events (44 named), 250 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/naval/effects/ai/hit_big` | Distance, is_hit_ours |
| `event:/naval/effects/ai/hit_mgun` | Distance, is_hit_ours |
| `event:/naval/effects/ai/hit_mid` | Distance, is_hit_ours |
| `event:/naval/effects/ai/hit_small` | is_hit_ours, Distance |
| `event:/naval/effects/alarm_battle` | pitch_mod |
| `event:/naval/effects/alarm_depth` | depth_alarm_dist |
| `event:/naval/effects/alarm_fire` | has_extinguisher, danger, fade_off |
| `event:/naval/effects/alarm_launch_fail` |  |
| `event:/naval/effects/art_shells_incoming` | Direction |
| `event:/naval/effects/bomb_drop` | Distance |
| `event:/naval/effects/bullethit_metal` | intense, Distance |
| `event:/naval/effects/buzzer` |  |
| `event:/naval/effects/camera_cross_water` | depth |
| `event:/naval/effects/collision_ship` | material, intense, Distance |
| `event:/naval/effects/collision_ship_wood` | intense, Distance |
| `event:/naval/effects/collision_underwater` | Distance |
| `event:/naval/effects/collision_water` | Distance, intense |
| `event:/naval/effects/collision_wave_boat` | on_wave, Distance, speed |
| `event:/naval/effects/collision_wave_ship` | Distance, on_wave, speed |
| `event:/naval/effects/countermeasures` | Distance, depth |
| `event:/naval/effects/extinguish` |  |
| `event:/naval/effects/hit_big` | Distance |
| `event:/naval/effects/hit_mgun` | Distance |
| `event:/naval/effects/hit_mid` | Distance |
| `event:/naval/effects/hit_small` | Distance |
| `event:/naval/effects/hydrophone/destroyer_01` | depth, gain, volume |
| `event:/naval/effects/main_caliber_distant` | Distance, Direction, timeline |
| `event:/naval/effects/main_caliber_hit` | Distance, intense |
| `event:/naval/effects/object_sink` | Distance |
| `event:/naval/effects/reload_cannon` |  |
| `event:/naval/effects/reload_cannon_manual` |  |
| `event:/naval/effects/reload_gun` |  |
| `event:/naval/effects/repair` |  |
| `event:/naval/effects/scrape` | Distance, material, intense |
| `event:/naval/effects/scrape_wood` | Distance, material, intense |
| `event:/naval/effects/shell_camera` | Distance, time |
| `event:/naval/effects/sink` | Distance |
| `event:/naval/effects/sink_old` | Distance |
| `event:/naval/effects/sonar` | depth |
| `event:/naval/effects/sonar_response` |  |
| `event:/naval/effects/telegraph_ring` |  |
| `event:/naval/effects/turret_turn` | velV, velH, Distance |
| `event:/naval/effects/turret_turn_big` | velH, broken, velV, Distance |
| `event:/naval/effects/turret_turn_servo` | Distance, velV, broken, velH |

## ships_engines

38 events (38 named), 92 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/naval/engines/ai_big/engine` | speed, Distance, broken, loadswitch, load, rpm |
| `event:/naval/engines/ai_ctr/engine` | load, rpm, speed, Distance |
| `event:/naval/engines/ai_ctr_jet/engine` | speed, Distance, load, rpm |
| `event:/naval/engines/ai_karotei/engine` | load, Event Cone Angle, rpm, speed, Distance |
| `event:/naval/engines/ai_karotei/engine_start` | Distance |
| `event:/naval/engines/ai_karotei/engine_stop` | Distance |
| `event:/naval/engines/ai_light/engine` | rpm, load, Distance, speed |
| `event:/naval/engines/ai_mid/engine` | speed, Distance, broken, loadswitch, load, rpm |
| `event:/naval/engines/ai_submarine/engine` | depth, Distance, load, rpm |
| `event:/naval/engines/ctr01/engine` | broken, loadswitch, Distance, speed, load, Event Cone Angle, rpm |
| `event:/naval/engines/ctr01/engine_interior` | rpm, load, loadswitch, broken, Distance, speed |
| `event:/naval/engines/ctr03/engine` | rpm, Event Cone Angle, load, loadswitch, broken, speed, Distance |
| `event:/naval/engines/ctr03/engine_interior` | load, rpm, speed, Distance, broken, loadswitch |
| `event:/naval/engines/pt15/engine` | load, rpm, Event Cone Angle, broken, loadswitch, speed, Distance |
| `event:/naval/engines/pt15/engine_interior` | rpm, load, loadswitch, broken, Distance, speed |
| `event:/naval/engines/ship_karotei/engine` | loadswitch, broken, Distance, speed, Event Cone Angle, rpm, load |
| `event:/naval/engines/ship_karotei/engine12` | Event Cone Angle, load, rpm, zoom, Distance, is_aero_on, event_vertical_angle, depth |
| `event:/naval/engines/ship_karotei/engine12_prop` | Distance |
| `event:/naval/engines/ship_karotei/engine12_start` | load, Event Cone Angle, Distance |
| `event:/naval/engines/ship_karotei/engine12_stop` | Distance |
| `event:/naval/engines/ship_karotei/engine_interior` | load, rpm, speed, Distance, broken, loadswitch |
| `event:/naval/engines/shipbig01/engine` | load, rpm, Event Cone Angle, speed, Distance, broken, loadswitch |
| `event:/naval/engines/shipbig01/engine_interior` | Distance, speed, loadswitch, broken, rpm, load |
| `event:/naval/engines/shiplight01/engine` | broken, loadswitch, Distance, speed, load, Event Cone Angle, rpm |
| `event:/naval/engines/shiplight01/engine_interior` | speed, Distance, loadswitch, broken, rpm, load |
| `event:/naval/engines/shipmid01/engine` | Event Cone Angle, rpm, load, loadswitch, broken, Distance, speed |
| `event:/naval/engines/shipmid01/engine_interior` | load, rpm, broken, loadswitch, speed, Distance |
| `event:/naval/engines/submarine/engine` | broken, loadswitch, speed, Distance, depth, load, rpm |
| `event:/naval/engines/tracks_ai_big` | turn, Distance, speed |
| `event:/naval/engines/tracks_ai_ctr` | speed, Distance, turn |
| `event:/naval/engines/tracks_ai_light` | turn, speed, Distance |
| `event:/naval/engines/tracks_ai_mid` | speed, Distance, turn |
| `event:/naval/engines/tracks_ai_submarine` | turn, Distance, depth, speed |
| `event:/naval/engines/tracks_big` | speed, Distance, turn, Event Cone Angle |
| `event:/naval/engines/tracks_ctr` | speed, Distance, Event Cone Angle, turn |
| `event:/naval/engines/tracks_light` | Distance, speed, Event Cone Angle, turn |
| `event:/naval/engines/tracks_mid` | speed, Distance, Event Cone Angle, turn |
| `event:/naval/engines/tracks_submarine` | turn, depth, Distance, speed |

## ships_explosions

38 events (22 named), 141 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/naval/effects/underwater_explosion` | Distance, depth |
| `event:/naval/explosions/ammo_explode` | Distance |
| `event:/naval/explosions/ammo_explode_med` | Distance |
| `event:/naval/explosions/ammo_explode_small` | Distance |
| `event:/naval/explosions/boiler_explode` | Distance |
| `event:/naval/explosions/boiler_steam` | Distance |
| `event:/naval/explosions/bomb_expl_underwater` | headphones, Distance, Direction |
| `event:/naval/explosions/destroy` | Distance |
| `event:/naval/explosions/engine_burn` | Distance |
| `event:/naval/explosions/fire_big` | Distance |
| `event:/naval/explosions/fire_destroyed` | Distance |
| `event:/naval/explosions/fire_huge` | Distance |
| `event:/naval/explosions/fire_massive` | Distance |
| `event:/naval/explosions/fire_med` | Distance |
| `event:/naval/explosions/fire_small` | Distance |
| `event:/naval/explosions/fire_tiny` | Distance |
| `event:/naval/explosions/mine_explosion` | Distance, intense |
| `event:/naval/explosions/ship_expl_large` | Distance |
| `event:/naval/explosions/underwater_destroyed` | Distance, headphones, depth, Direction |
| `event:/naval/explosions/underwater_expl_heavy` | Direction, depth, headphones, Distance |
| `event:/naval/explosions/underwater_expl_med` | headphones, Distance, Direction, depth |
| `event:/naval/explosions/underwater_expl_small` | Direction, depth, headphones, Distance |

## ships_weapon

204 events (123 named), 1202 waveforms.

| Event | Parameters |
| --- | --- |
| `event:/naval/weapon/atgm/atgm` | building_density, on_shot, Event Cone Angle, Distance |
| `event:/naval/weapon/atgm/atgm_ai` | Direction, building_density, on_shot, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/100mm_d10t` | multiply_weapon, on_shot, Event Cone Angle, Distance, headphones |
| `event:/naval/weapon/cannons/100mm_d10t_ai` | on_shot, multiply_weapon, Direction, headphones, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/105mm_kwk46` | headphones, Distance, Event Cone Angle, on_shot, multiply_weapon |
| `event:/naval/weapon/cannons/105mm_kwk46_ai` | Direction, multiply_weapon, on_shot, Event Cone Angle, Distance, headphones |
| `event:/naval/weapon/cannons/114mm_8cwt_qf` | multiply_weapon, on_shot, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/114mm_8cwt_qf_ai` | Direction, on_shot, multiply_weapon, Event Cone Angle, Distance, headphones |
| `event:/naval/weapon/cannons/128mm_pak44` | headphones, Event Cone Angle, Distance, building_density, on_shot, multiply_weapon |
| `event:/naval/weapon/cannons/128mm_pak44_ai` | on_shot, multiply_weapon, building_density, Direction, Distance, Event Cone Angle, headphones |
| `event:/naval/weapon/cannons/130mm_b13` | headphones, Event Cone Angle, Distance, on_shot, multiply_weapon |
| `event:/naval/weapon/cannons/130mm_b13_ai` | multiply_weapon, on_shot, Direction, Distance, Event Cone Angle, headphones |
| `event:/naval/weapon/cannons/152mm_ml20` | Distance, Event Cone Angle, headphones, on_shot, multiply_weapon |
| `event:/naval/weapon/cannons/152mm_ml20_ai` | headphones, Event Cone Angle, Distance, Direction, on_shot, multiply_weapon |
| `event:/naval/weapon/cannons/180mm_b1k` | on_shot, multiply_weapon, Distance, Event Cone Angle, headphones |
| `event:/naval/weapon/cannons/180mm_b1k_ai` | headphones, Distance, Event Cone Angle, on_shot, multiply_weapon, Direction |
| `event:/naval/weapon/cannons/20mm_breda_20_65` | Event Cone Angle, Distance, headphones, building_density, on_shot |
| `event:/naval/weapon/cannons/20mm_breda_20_65_ai` | headphones, Event Cone Angle, Distance, on_shot, Direction, building_density |
| `event:/naval/weapon/cannons/20mm_m61` | Event Cone Angle, Distance, fast, headphones, building_density, on_shot |
| `event:/naval/weapon/cannons/20mm_m61_ai` | on_shot, building_density, Direction, fast, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/20mm_m61_rotor` | on_shot, building_density, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/20mm_m61_rotor_ai` | on_shot, Distance |
| `event:/naval/weapon/cannons/20mm_m61_slow` | building_density, on_shot, Event Cone Angle, Distance, fast, headphones |
| `event:/naval/weapon/cannons/20mm_m61_slow_ai` | fast, headphones, Event Cone Angle, Distance, on_shot, building_density, Direction |
| `event:/naval/weapon/cannons/20mm_m61_slow_rotor` | Event Cone Angle, Distance, building_density, on_shot |
| `event:/naval/weapon/cannons/20mm_m61_slow_rotor_ai` | on_shot, Distance |
| `event:/naval/weapon/cannons/20mm_mg_c38` | Event Cone Angle, Distance, headphones, building_density, on_shot |
| `event:/naval/weapon/cannons/20mm_mg_c38_ai` | headphones, Event Cone Angle, Distance, on_shot, Direction, building_density |
| `event:/naval/weapon/cannons/20mm_oerlikon` | Event Cone Angle, Distance, headphones, building_density, on_shot |
| `event:/naval/weapon/cannons/20mm_oerlikon_ai` | on_shot, Direction, building_density, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/20mm_rh202` | headphones, Event Cone Angle, Distance, on_shot, building_density |
| `event:/naval/weapon/cannons/20mm_rh202_ai` | on_shot, building_density, Direction, headphones, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/20mm_tnsh` | headphones, Event Cone Angle, Distance, on_shot, building_density |
| `event:/naval/weapon/cannons/20mm_tnsh_ai` | on_shot, Direction, building_density, headphones, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/23mm_2a14` | Event Cone Angle, Distance, headphones, building_density, on_shot |
| `event:/naval/weapon/cannons/23mm_2a14_ai` | Event Cone Angle, Distance, headphones, building_density, Direction, on_shot |
| `event:/naval/weapon/cannons/25mm_2m_3` | building_density, on_shot, Distance, Event Cone Angle, headphones |
| `event:/naval/weapon/cannons/25mm_2m_3_ai` | headphones, Distance, Event Cone Angle, on_shot, building_density, Direction |
| `event:/naval/weapon/cannons/25mm_mark_38` | headphones, Distance, Event Cone Angle, on_shot, building_density |
| `event:/naval/weapon/cannons/25mm_mark_38_ai` | Event Cone Angle, Distance, headphones, building_density, Direction, on_shot |
| `event:/naval/weapon/cannons/25mm_type_96` | on_shot, building_density, headphones, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/25mm_type_96_ai` | Distance, Event Cone Angle, headphones, building_density, Direction, on_shot |
| `event:/naval/weapon/cannons/280mm_52_sck_28` | headphones, Distance, Event Cone Angle, multiply_weapon, on_shot |
| `event:/naval/weapon/cannons/280mm_52_sck_28_ai` | multiply_weapon, on_shot, Direction, Distance, Event Cone Angle, headphones |
| `event:/naval/weapon/cannons/30mm_ak630` | headphones, fast, Distance, Event Cone Angle, on_shot, building_density |
| `event:/naval/weapon/cannons/30mm_ak630_ai` | on_shot, building_density, Direction, headphones, fast, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/30mm_ak630_rotor` | on_shot, building_density, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/30mm_ak630_rotor_ai` | Distance, on_shot |
| `event:/naval/weapon/cannons/30mm_mk103_38` | on_shot, building_density, headphones, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/30mm_mk103_38_ai` | on_shot, Direction, building_density, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/356mm_45_mk8` | multiply_weapon, on_shot, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/356mm_45_mk8_ai` | on_shot, multiply_weapon, Direction, headphones, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/35mm_oerlikon_kda` | on_shot, building_density, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/35mm_oerlikon_kda_ai` | Distance, Event Cone Angle, headphones, Direction, building_density, on_shot |
| `event:/naval/weapon/cannons/37mm_flakm42` | headphones, Distance, Event Cone Angle, multiply_weapon, on_shot |
| `event:/naval/weapon/cannons/37mm_flakm42_ai` | headphones, Event Cone Angle, Distance, Direction, multiply_weapon, on_shot |
| `event:/naval/weapon/cannons/37mm_sh37` | headphones, Distance, Event Cone Angle, on_shot, multiply_weapon |
| `event:/naval/weapon/cannons/37mm_sh37_ai` | on_shot, multiply_weapon, Direction, Distance, Event Cone Angle, headphones |
| `event:/naval/weapon/cannons/40mm_l60_bofors` | on_shot, multiply_weapon, headphones, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/40mm_l60_bofors_ai` | Event Cone Angle, Distance, headphones, Direction, on_shot, multiply_weapon |
| `event:/naval/weapon/cannons/40mm_l70_bofors_mel_58` | Event Cone Angle, Distance, headphones, building_density, on_shot |
| `event:/naval/weapon/cannons/40mm_l70_bofors_mel_58_ai` | Distance, Event Cone Angle, headphones, building_density, Direction, on_shot |
| `event:/naval/weapon/cannons/40mm_qf_2pdr_mk_xv` | multiply_weapon, on_shot, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/40mm_qf_2pdr_mk_xv_ai` | Direction, multiply_weapon, on_shot, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/410mm_45_type_3` | headphones, Event Cone Angle, Distance, multiply_weapon, on_shot |
| `event:/naval/weapon/cannons/410mm_45_type_3_ai` | on_shot, multiply_weapon, Direction, headphones, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/45mm_20k` | headphones, Distance, Event Cone Angle, on_shot, multiply_weapon |
| `event:/naval/weapon/cannons/45mm_20k_ai` | Event Cone Angle, Distance, headphones, Direction, on_shot, multiply_weapon |
| `event:/naval/weapon/cannons/460mm_45_type_94` | Distance, Event Cone Angle, headphones, multiply_weapon, on_shot |
| `event:/naval/weapon/cannons/460mm_45_type_94_ai` | Direction, on_shot, multiply_weapon, Event Cone Angle, Distance, headphones |
| `event:/naval/weapon/cannons/50mm_kwk39` | on_shot, multiply_weapon, Distance, Event Cone Angle, headphones |
| `event:/naval/weapon/cannons/50mm_kwk39_ai` | Direction, multiply_weapon, on_shot, Event Cone Angle, Distance, headphones |
| `event:/naval/weapon/cannons/57mm_qf6` | on_shot, multiply_weapon, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/57mm_qf6_ai` | multiply_weapon, on_shot, Direction, Distance, Event Cone Angle, headphones |
| `event:/naval/weapon/cannons/57mm_zis4` | on_shot, multiply_weapon, Distance, Event Cone Angle, headphones |
| `event:/naval/weapon/cannons/57mm_zis4_ai` | headphones, Distance, Event Cone Angle, multiply_weapon, on_shot, Direction |
| `event:/naval/weapon/cannons/75mm_m3` | multiply_weapon, on_shot, Distance, Event Cone Angle, headphones |
| `event:/naval/weapon/cannons/75mm_m3_ai` | Direction, on_shot, multiply_weapon, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/76mm_f34` | headphones, Distance, Event Cone Angle, multiply_weapon, on_shot |
| `event:/naval/weapon/cannons/76mm_f34_1124` | multiply_weapon, on_shot, Event Cone Angle, Distance, headphones |
| `event:/naval/weapon/cannons/76mm_f34_1124_ai` | multiply_weapon, on_shot, Direction, headphones, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/76mm_f34_ai` | Distance, Event Cone Angle, headphones, multiply_weapon, on_shot, Direction |
| `event:/naval/weapon/cannons/76mm_qf17` | Distance, Event Cone Angle, headphones, on_shot, multiply_weapon |
| `event:/naval/weapon/cannons/76mm_qf17_ai` | headphones, Distance, Event Cone Angle, multiply_weapon, on_shot, Direction |
| `event:/naval/weapon/cannons/76mm_qqf` | on_shot, multiply_weapon, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/76mm_qqf_ai` | headphones, Distance, Event Cone Angle, multiply_weapon, on_shot, Direction |
| `event:/naval/weapon/cannons/85mm_zis_s_53` | multiply_weapon, on_shot, headphones, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/85mm_zis_s_53_ai` | Direction, on_shot, multiply_weapon, headphones, Event Cone Angle, Distance |
| `event:/naval/weapon/cannons/88mm_kwk36` | on_shot, multiply_weapon, headphones, Distance, Event Cone Angle |
| `event:/naval/weapon/cannons/88mm_kwk36_ai` | Distance, Event Cone Angle, headphones, multiply_weapon, on_shot, Direction |
| `event:/naval/weapon/cannons/grenade_launcher` | Distance, Event Cone Angle, headphones, on_shot |
| `event:/naval/weapon/cannons/grenade_launcher_ai` | Distance, Event Cone Angle, headphones, on_shot, Direction |
| `event:/naval/weapon/mguns/12mm_m2` | Distance, guns, headphones, building_density, on_shot |
| `event:/naval/weapon/mguns/12mm_m2_ai` | Distance, guns, headphones, building_density, Direction, on_shot |
| `event:/naval/weapon/mguns/13mm_dshk` | guns, Distance, headphones, building_density, on_shot |
| `event:/naval/weapon/mguns/13mm_dshk_ai` | headphones, Distance, guns, on_shot, building_density, Direction |
| `event:/naval/weapon/mguns/13mm_hotchkiss` | headphones, Distance, guns, on_shot, building_density |
| `event:/naval/weapon/mguns/13mm_hotchkiss_ai` | guns, Distance, headphones, building_density, Direction, on_shot |
| `event:/naval/weapon/mguns/13mm_vickers_mkv` | on_shot, building_density, headphones, Distance, guns |
| `event:/naval/weapon/mguns/13mm_vickers_mkv_ai` | headphones, Distance, guns, on_shot, building_density, Direction |
| `event:/naval/weapon/mguns/15mm_mg151` | headphones, Distance, guns, on_shot, building_density |
| `event:/naval/weapon/mguns/15mm_mg151_ai` | headphones, Distance, guns, on_shot, building_density, Direction |
| `event:/naval/weapon/mguns/16mm_kpvt` | on_shot, building_density, headphones, Distance, guns |
| `event:/naval/weapon/mguns/16mm_kpvt_ai` | guns, Distance, headphones, building_density, Direction, on_shot |
| `event:/naval/weapon/mguns/8mm_breda_mod30` | headphones, Distance, guns, on_shot, building_density |
| `event:/naval/weapon/mguns/8mm_breda_mod30_ai` | Direction, building_density, on_shot, guns, Distance, headphones |
| `event:/naval/weapon/mguns/8mm_m1918` | headphones, Distance, guns, on_shot, building_density |
| `event:/naval/weapon/mguns/8mm_m1918_ai` | on_shot, Direction, building_density, headphones, guns, Distance |
| `event:/naval/weapon/mguns/8mm_m1919` | Distance, guns, headphones, building_density, on_shot |
| `event:/naval/weapon/mguns/8mm_m1919_ai` | Direction, building_density, on_shot, Distance, guns, headphones |
| `event:/naval/weapon/mguns/8mm_mg34` | headphones, Distance, guns, on_shot, building_density |
| `event:/naval/weapon/mguns/8mm_mg34_ai` | Distance, guns, headphones, building_density, Direction, on_shot |
| `event:/naval/weapon/mguns/8mm_vickers303` | on_shot, building_density, headphones, guns, Distance |
| `event:/naval/weapon/mguns/8mm_vickers303_ai` | guns, Distance, headphones, building_density, Direction, on_shot |
| `event:/naval/weapon/rockets/75mm_m3` | Distance, Event Cone Angle, headphones, on_shot |
| `event:/naval/weapon/rockets/75mm_m3_ai` | Distance, Event Cone Angle, headphones, on_shot, Direction |
| `event:/naval/weapon/rockets/bm_13` | on_shot, Distance, Event Cone Angle, headphones |
| `event:/naval/weapon/rockets/bm_13_ai` | Event Cone Angle, Distance, headphones, Direction, on_shot |
| `event:/naval/weapon/rockets/rgb_60` | headphones, Distance, Event Cone Angle, on_shot |
| `event:/naval/weapon/rockets/rgb_60_ai` | on_shot, Direction, headphones, Distance, Event Cone Angle |
| `event:/naval/weapon/rockets/slbm` | on_shot, Event Cone Angle, Distance |
| `event:/naval/weapon/rockets/slbm_ai` | on_shot, Distance, Event Cone Angle |
| `event:/naval/weapon/rockets/slbm_fly` | Event Cone Angle, Distance, depth |
