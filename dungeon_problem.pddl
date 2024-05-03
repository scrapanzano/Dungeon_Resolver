(define (problem instance_20_1229)
  (:domain dungeon)

  ;Objects and their hierarchy 
  (:objects
    R0 R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 R16 R17 R18 R19 - room
    T0 T1 T2 T3 T4 T5 T6 T7 - treasure
    E0 E1 E2 E3 E4 E5 E6 E7 - enemy 
    W0 W1 W2 W3 W4 W5 W6 W7 - weapon
    P0 P1 P2 P3 P4 P5 P6 P7 - potion 
  )

  ;Initial state's facts and numeric values
  (:init
    ;Hero initial position
    (at R0)
    ;Dungeon exit room
    (exit_room R9)
    ;Connected rooms (no door between them)
    (connected R0 R2) (connected R1 R2) (connected R2 R1) (connected R2 R0) (connected R2 R4) (connected R3 R18) (connected R4 R2) (connected R4 R7) (connected R5 R6) (connected R6 R5) (connected R7 R4) (connected R8 R9) (connected R9 R8) (connected R9 R10) (connected R10 R9) (connected R10 R11) (connected R10 R12) (connected R11 R10) (connected R11 R13) (connected R12 R10) (connected R12 R14) (connected R13 R11) (connected R14 R15) (connected R14 R12) (connected R15 R14) (connected R15 R16) (connected R15 R17) (connected R16 R15) (connected R16 R17) (connected R16 R18) (connected R17 R16) (connected R17 R18) (connected R17 R15) (connected R17 R19) (connected R18 R17) (connected R18 R19) (connected R18 R16) (connected R18 R3) (connected R19 R18) (connected R19 R17) 
    ;Safe rooms (no enemies inside)
    (room_safe R0) (room_safe R1) (room_safe R4) (room_safe R5) (room_safe R10) (room_safe R12) (room_safe R14) (room_safe R15) (room_safe R16) (room_safe R17) (room_safe R18) (room_safe R19)  
    ;Closed door between rooms (rooms are initially not connected)
    (closed_door R0 R1) (closed_door R0 R18) (closed_door R1 R0) (closed_door R1 R3) (closed_door R1 R19) (closed_door R2 R3) (closed_door R3 R2) (closed_door R3 R4) (closed_door R3 R1) (closed_door R4 R3) (closed_door R4 R5) (closed_door R4 R6) (closed_door R4 R19) (closed_door R5 R4) (closed_door R5 R7) (closed_door R6 R4) (closed_door R6 R8) (closed_door R6 R12) (closed_door R7 R5) (closed_door R7 R18) (closed_door R8 R6) (closed_door R8 R10) (closed_door R9 R11) (closed_door R10 R8) (closed_door R11 R12) (closed_door R11 R9) (closed_door R12 R11) (closed_door R12 R13) (closed_door R12 R6) (closed_door R13 R12) (closed_door R13 R14) (closed_door R13 R15) (closed_door R14 R13) (closed_door R14 R16) (closed_door R15 R13) (closed_door R16 R14) (closed_door R18 R0) (closed_door R18 R7) (closed_door R19 R1) (closed_door R19 R4) 
    ;Keys position and counter
    
    (= (key_counter) 0)
    ;Treasures position and value
    (treasure_at T0 R7) (treasure_at T1 R1) (treasure_at T2 R3) (treasure_at T3 R6) (treasure_at T4 R13) (treasure_at T5 R8) (treasure_at T6 R11) (treasure_at T7 R2) 
    (= (treasure_value T0) 20) (= (treasure_value T1) 10) (= (treasure_value T2) 20) (= (treasure_value T3) 40) (= (treasure_value T4) 20) (= (treasure_value T5) 20) (= (treasure_value T6) 10) (= (treasure_value T7) 40) 
    ;Enemies position and stats
    (enemy_at E0 R2) (enemy_at E1 R6) (enemy_at E2 R13) (enemy_at E3 R3) (enemy_at E4 R9) (enemy_at E5 R7) (enemy_at E6 R11) (enemy_at E7 R8)  
    (= (enemy_life E0) 90) (= (enemy_life E1) 30) (= (enemy_life E2) 50) (= (enemy_life E3) 90) (= (enemy_life E4) 50) (= (enemy_life E5) 90) (= (enemy_life E6) 90) (= (enemy_life E7) 50)  
    (= (enemy_strength E0) 90) (= (enemy_strength E1) 30) (= (enemy_strength E2) 50) (= (enemy_strength E3) 90) (= (enemy_strength E4) 50) (= (enemy_strength E5) 90) (= (enemy_strength E6) 90) (= (enemy_strength E7) 50) 
    ;Weapons position and strength
    (weapon_at W0 R16) (weapon_at W1 R15) (weapon_at W2 R4) (weapon_at W3 R10) (weapon_at W4 R1) (weapon_at W5 R12) (weapon_at W6 R17) (weapon_at W7 R14)  
    (= (weapon_strength W0) 90) (= (weapon_strength W1) 30) (= (weapon_strength W2) 50) (= (weapon_strength W3) 90) (= (weapon_strength W4) 50) (= (weapon_strength W5) 90) (= (weapon_strength W6) 90) (= (weapon_strength W7) 50) 
    ;Potions position and value
    (potion_at P0 R15) (potion_at P1 R17) (potion_at P2 R16) (potion_at P3 R11) (potion_at P4 R12) (potion_at P5 R9) (potion_at P6 R6) (potion_at P7 R7)  
    (= (potion_value P0) 50) (= (potion_value P1) 30) (= (potion_value P2) 10) (= (potion_value P3) 30) (= (potion_value P4) 30) (= (potion_value P5) 50) (= (potion_value P6) 10) (= (potion_value P7) 50) 
    (= (potion_counter) 0)
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
      (>= (hero_loot) 62)
      (> (hero_life) 0)
      (>= (defeated_enemy_counter) 1)
    )
  )
)