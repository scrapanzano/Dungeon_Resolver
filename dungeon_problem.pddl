(define (problem instance_15_1229)
  (:domain dungeon)

  ;Objects and their hierarchy 
  (:objects
    R0 R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 - room
    T0 T1 T2 T3 T4 T5 - treasure
    E0 E1 E2 E3 E4 E5 - enemy 
    W0 W1 W2 W3 W4 W5 - weapon
    P0 P1 P2 P3 P4 P5 - potion 
  )

  ;Initial state's facts and numeric values
  (:init
    ;Hero initial position
    (at R0)
    ;Dungeon exit room
    (exit_room R10)
    ;Connected rooms (no door between them)
    (connected R0 R1) (connected R0 R2) (connected R1 R0) (connected R1 R2) (connected R1 R3) (connected R2 R1) (connected R2 R3) (connected R2 R0) (connected R3 R2) (connected R3 R4) (connected R3 R1) (connected R4 R3) (connected R4 R5) (connected R5 R4) (connected R6 R8) (connected R8 R9) (connected R8 R6) (connected R9 R8) (connected R9 R11) (connected R10 R11) (connected R11 R10) (connected R11 R9) (connected R13 R14) (connected R14 R13) 
    ;Safe rooms (no enemies inside)
    (room_safe R0) (room_safe R2) (room_safe R4) (room_safe R6) (room_safe R7) (room_safe R11) (room_safe R12) (room_safe R13) (room_safe R14)  
    ;Closed door between rooms (rooms are initially not connected)
    (closed_door R0 R14) (closed_door R0 R13) (closed_door R0 R6) (closed_door R1 R14) (closed_door R2 R4) (closed_door R2 R7) (closed_door R3 R5) (closed_door R4 R2) (closed_door R4 R7) (closed_door R5 R6) (closed_door R5 R3) (closed_door R5 R7) (closed_door R6 R5) (closed_door R6 R0) (closed_door R7 R8) (closed_door R7 R5) (closed_door R7 R4) (closed_door R7 R2) (closed_door R8 R7) (closed_door R8 R10) (closed_door R9 R10) (closed_door R9 R12) (closed_door R10 R9) (closed_door R10 R8) (closed_door R10 R12) (closed_door R11 R12) (closed_door R11 R13) (closed_door R12 R11) (closed_door R12 R13) (closed_door R12 R10) (closed_door R12 R9) (closed_door R13 R12) (closed_door R13 R11) (closed_door R13 R0) (closed_door R14 R0) (closed_door R14 R1) 
    ;Keys position and counter
    (key_at R2) 
    (= (key_counter) 0)
    ;Treasures position and value
    (treasure_at T0 R4) (treasure_at T1 R12) (treasure_at T2 R11) (treasure_at T3 R10) (treasure_at T4 R2) (treasure_at T5 R7) 
    (= (treasure_value T0) 10) (= (treasure_value T1) 20) (= (treasure_value T2) 20) (= (treasure_value T3) 10) (= (treasure_value T4) 40) (= (treasure_value T5) 40) 
    ;Enemies position and stats
    (enemy_at E0 R9) (enemy_at E1 R8) (enemy_at E2 R5) (enemy_at E3 R3) (enemy_at E4 R10) (enemy_at E5 R1)  
    (= (enemy_life E0) 50) (= (enemy_life E1) 90) (= (enemy_life E2) 90) (= (enemy_life E3) 50) (= (enemy_life E4) 30) (= (enemy_life E5) 50)  
    (= (enemy_strength E0) 50) (= (enemy_strength E1) 90) (= (enemy_strength E2) 90) (= (enemy_strength E3) 50) (= (enemy_strength E4) 30) (= (enemy_strength E5) 50) 
    ;Weapons position and strength
    (weapon_at W0 R2) (weapon_at W1 R4) (weapon_at W2 R7) (weapon_at W3 R13) (weapon_at W4 R6) (weapon_at W5 R11)  
    (= (weapon_strength W0) 50) (= (weapon_strength W1) 90) (= (weapon_strength W2) 90) (= (weapon_strength W3) 50) (= (weapon_strength W4) 30) (= (weapon_strength W5) 50) 
    ;Potions position and value
    (potion_at P0 R14) (potion_at P1 R1) (potion_at P2 R3) (potion_at P3 R10) (potion_at P4 R7) (potion_at P5 R4)  
    (= (potion_value P0) 10) (= (potion_value P1) 10) (= (potion_value P2) 30) (= (potion_value P3) 10) (= (potion_value P4) 50) (= (potion_value P5) 10) 
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
      (>= (hero_loot) 49)
      (> (hero_life) 0)
      (>= (defeated_enemy_counter) 1)
    )
  )
)