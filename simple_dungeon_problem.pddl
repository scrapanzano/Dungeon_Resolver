(define (problem instance_30_1229)
  (:domain simple_dungeon)

  ;Objects and their hierarchy 
  (:objects
    R0 R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 R16 R17 R18 R19 R20 R21 R22 R23 R24 R25 R26 R27 R28 R29 - room
    T0 T1 T2 T3 T4 T5 T6 T7 T8 T9 T10 T11 - treasure
    E0 E1 E2 E3 E4 E5 E6 E7 E8 E9 E10 E11 - enemy 
    W0 W1 W2 W3 W4 W5 W6 W7 W8 W9 W10 W11 - weapon
    P0 P1 P2 P3 P4 P5 P6 P7 P8 P9 P10 P11 - potion 
  )

  ;Initial state's facts and numeric values
  (:init
    ;Hero initial position
    (at R0)
    ;Dungeon exit room
    (exit_room R10)
    ;Connected rooms (no door between them)
    (connected R0 R1) (connected R0 R2) (connected R0 R28) (connected R1 R0) (connected R1 R3) (connected R2 R3) (connected R2 R0) (connected R3 R2) (connected R3 R4) (connected R3 R1) (connected R4 R3) (connected R4 R5) (connected R4 R6) (connected R4 R7) (connected R4 R19) (connected R4 R22) (connected R5 R4) (connected R5 R6) (connected R5 R7) (connected R6 R5) (connected R6 R4) (connected R6 R8) (connected R6 R12) (connected R7 R5) (connected R7 R4) (connected R8 R9) (connected R8 R6) (connected R8 R10) (connected R9 R8) (connected R10 R8) (connected R10 R12) (connected R11 R12) (connected R12 R11) (connected R12 R13) (connected R12 R10) (connected R12 R6) (connected R13 R12) (connected R13 R14) (connected R13 R15) (connected R14 R13) (connected R15 R16) (connected R15 R13) (connected R16 R15) (connected R16 R17) (connected R16 R18) (connected R17 R16) (connected R17 R18) (connected R18 R17) (connected R18 R19) (connected R18 R16) (connected R18 R20) (connected R19 R18) (connected R19 R21) (connected R19 R4) (connected R20 R21) (connected R20 R18) (connected R20 R22) (connected R21 R20) (connected R21 R22) (connected R21 R19) (connected R21 R23) (connected R22 R21) (connected R22 R23) (connected R22 R20) (connected R22 R4) (connected R23 R22) (connected R23 R21) (connected R23 R25) (connected R24 R25) (connected R24 R26) (connected R24 R27) (connected R25 R24) (connected R25 R23) (connected R26 R27) (connected R26 R24) (connected R27 R26) (connected R27 R29) (connected R27 R24) (connected R28 R0) (connected R29 R27) 
    ;Safe rooms (no enemies inside)
    (room_safe R0) (room_safe R1) (room_safe R4) (room_safe R6) (room_safe R7) (room_safe R8) (room_safe R9) (room_safe R10) (room_safe R11) (room_safe R12) (room_safe R13) (room_safe R17) (room_safe R18) (room_safe R20) (room_safe R21) (room_safe R26) (room_safe R27) (room_safe R28)  
    ;Closed door between rooms (rooms are initially not connected)
    (closed_door R0 R29) (closed_door R1 R2) (closed_door R1 R29) (closed_door R2 R1) (closed_door R2 R4) (closed_door R2 R23) (closed_door R3 R5) (closed_door R4 R2) (closed_door R5 R3) (closed_door R6 R11) (closed_door R7 R9) (closed_door R9 R10) (closed_door R9 R7) (closed_door R9 R11) (closed_door R10 R9) (closed_door R10 R11) (closed_door R11 R10) (closed_door R11 R9) (closed_door R11 R6) (closed_door R12 R14) (closed_door R14 R15) (closed_door R14 R12) (closed_door R14 R16) (closed_door R15 R14) (closed_door R15 R17) (closed_door R16 R14) (closed_door R17 R15) (closed_door R17 R19) (closed_door R19 R17) (closed_door R23 R2) (closed_door R25 R26) (closed_door R25 R27) (closed_door R26 R25) (closed_door R26 R28) (closed_door R27 R25) (closed_door R28 R29) (closed_door R28 R26) (closed_door R29 R28) (closed_door R29 R0) (closed_door R29 R1) 
    ;Keys position and counter
    (key_at R4) (key_at R8) (key_at R9) (key_at R12) (key_at R23) (key_at R26) (key_at R27) 
    (= (key_counter) 0)
    ;Treasures position and value
    (treasure_at T0 R20) (treasure_at T1 R17) (treasure_at T2 R5) (treasure_at T3 R14) (treasure_at T4 R26) (treasure_at T5 R2) (treasure_at T6 R11) (treasure_at T7 R28) (treasure_at T8 R24) (treasure_at T9 R13) (treasure_at T10 R27) (treasure_at T11 R7) 
    (= (treasure_value T0) 30) (= (treasure_value T1) 10) (= (treasure_value T2) 40) (= (treasure_value T3) 10) (= (treasure_value T4) 30) (= (treasure_value T5) 30) (= (treasure_value T6) 10) (= (treasure_value T7) 20) (= (treasure_value T8) 40) (= (treasure_value T9) 40) (= (treasure_value T10) 20) (= (treasure_value T11) 40) 
    ;Enemies position and stats
    (enemy_at E0 R16) (enemy_at E1 R5) (enemy_at E2 R22) (enemy_at E3 R25) (enemy_at E4 R3) (enemy_at E5 R2) (enemy_at E6 R23) (enemy_at E7 R14) (enemy_at E8 R24) (enemy_at E9 R15) (enemy_at E10 R19) (enemy_at E11 R29)  
    (= (enemy_life E0) 90) (= (enemy_life E1) 70) (= (enemy_life E2) 90) (= (enemy_life E3) 70) (= (enemy_life E4) 30) (= (enemy_life E5) 70) (= (enemy_life E6) 90) (= (enemy_life E7) 70) (= (enemy_life E8) 90) (= (enemy_life E9) 90) (= (enemy_life E10) 30) (= (enemy_life E11) 90)  
    (= (enemy_strength E0) 90) (= (enemy_strength E1) 70) (= (enemy_strength E2) 90) (= (enemy_strength E3) 70) (= (enemy_strength E4) 30) (= (enemy_strength E5) 70) (= (enemy_strength E6) 90) (= (enemy_strength E7) 70) (= (enemy_strength E8) 90) (= (enemy_strength E9) 90) (= (enemy_strength E10) 30) (= (enemy_strength E11) 90) 
    ;Weapons position and strength
    (weapon_at W0 R18) (weapon_at W1 R11) (weapon_at W2 R13) (weapon_at W3 R1) (weapon_at W4 R12) (weapon_at W5 R9) (weapon_at W6 R8) (weapon_at W7 R17) (weapon_at W8 R26) (weapon_at W9 R20) (weapon_at W10 R6) (weapon_at W11 R10)  
    (= (weapon_strength W0) 90) (= (weapon_strength W1) 70) (= (weapon_strength W2) 90) (= (weapon_strength W3) 70) (= (weapon_strength W4) 30) (= (weapon_strength W5) 70) (= (weapon_strength W6) 90) (= (weapon_strength W7) 70) (= (weapon_strength W8) 90) (= (weapon_strength W9) 90) (= (weapon_strength W10) 30) (= (weapon_strength W11) 90) 
    ;Potions position and value
    (potion_at P0 R23) (potion_at P1 R29) (potion_at P2 R7) (potion_at P3 R27) (potion_at P4 R9) (potion_at P5 R15) (potion_at P6 R28) (potion_at P7 R17) (potion_at P8 R14) (potion_at P9 R5) (potion_at P10 R3) (potion_at P11 R20)  
    (= (potion_value P0) 30) (= (potion_value P1) 50) (= (potion_value P2) 10) (= (potion_value P3) 50) (= (potion_value P4) 50) (= (potion_value P5) 30) (= (potion_value P6) 30) (= (potion_value P7) 50) (= (potion_value P8) 30) (= (potion_value P9) 30) (= (potion_value P10) 10) (= (potion_value P11) 10)  
    ;Hero initial stats 
    (= (hero_life) 100)
    (= (max_hero_life) 100)
    (= (hero_strength) 0)
    (= (hero_loot) 0)
    (= (defeated_enemy_counter) 0)
  )

  ;Goal condition
  (:goal
    (and
      (escape) 
      (>= (hero_loot) 112)
      (> (hero_life) 0)
      (>= (defeated_enemy_counter) 2)
    )
  )
)