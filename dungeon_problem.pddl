(define (problem instance_8_1229)
  (:domain dungeon)

  ;Objects and their hierarchy 
  (:objects
    R0 R1 R2 R3 R4 R5 R6 R7 - room
    T0 T1 T2 - treasure
    E0 E1 E2 - enemy 
    W0 W1 W2 - weapon
    P0 P1 P2 - potion 
  )

  ;Initial state's facts and numeric values
  (:init
    ;Hero initial position
    (at R0)
    ;Dungeon exit room
    (exit_room R3)
    ;Connected rooms (no door between them)
    (connected R0 R1) (connected R0 R7) (connected R0 R2) (connected R0 R6) (connected R1 R0) (connected R1 R2) (connected R1 R3) (connected R1 R7) (connected R2 R1) (connected R2 R3) (connected R2 R0) (connected R2 R4) (connected R3 R2) (connected R3 R4) (connected R3 R1) (connected R3 R5) (connected R4 R3) (connected R4 R5) (connected R4 R2) (connected R5 R4) (connected R5 R6) (connected R5 R3) (connected R6 R5) (connected R6 R0) (connected R7 R0) (connected R7 R1) 
    ;Safe rooms (no enemies inside)
    (room_safe R0) (room_safe R2) (room_safe R4) (room_safe R5) (room_safe R7)  
    ;Closed door between rooms (rooms are initially not connected)
    (closed_door R2 R6) (closed_door R4 R6) (closed_door R5 R7) (closed_door R6 R4) (closed_door R6 R2) (closed_door R7 R5) 
    ;Keys position and counter
    
    (= (key_counter) 0)
    ;Treasures position and value
    (treasure_at T0 R5) (treasure_at T1 R4) (treasure_at T2 R2) 
    (= (treasure_value T0) 30) (= (treasure_value T1) 40) (= (treasure_value T2) 40) 
    ;Enemies position and stats
    (enemy_at E0 R6) (enemy_at E1 R3) (enemy_at E2 R1)  
    (= (enemy_life E0) 70) (= (enemy_life E1) 50) (= (enemy_life E2) 50)  
    (= (enemy_strength E0) 70) (= (enemy_strength E1) 50) (= (enemy_strength E2) 50) 
    ;Weapons position and strength
    (weapon_at W0 R7) (weapon_at W1 R5) (weapon_at W2 R2)  
    (= (weapon_strength W0) 70) (= (weapon_strength W1) 50) (= (weapon_strength W2) 50) 
    ;Potions position and value
    (potion_at P0 R5) (potion_at P1 R4) (potion_at P2 R6)  
    (= (potion_value P0) 30) (= (potion_value P1) 10) (= (potion_value P2) 50)  
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
      (>= (hero_loot) 38)
      (> (hero_life) 0)
      (>= (defeated_enemy_counter) 0)
    )
  )
)