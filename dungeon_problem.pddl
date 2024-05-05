(define (problem instance_5_100)
  (:domain dungeon)

  ;Objects and their hierarchy 
  (:objects
    R0 R1 R2 R3 R4 - room
    T0 T1 - treasure
    E0 E1 - enemy 
    W0 W1 - weapon
    P0 P1 - potion 
  )

  ;Initial state's facts and numeric values
  (:init
    ;Hero initial position
    (at R0)
    ;Dungeon exit room
    (exit_room R1)
    ;Connected rooms (no door between them)
    (connected R0 R1) (connected R1 R0) (connected R1 R2) (connected R1 R4) (connected R2 R1) (connected R2 R3) (connected R3 R2) (connected R3 R4) (connected R4 R3) (connected R4 R1) 
    ;Safe rooms (no enemies inside)
    (room_safe R0) (room_safe R1) (room_safe R4)  
    ;Closed door between rooms (rooms are initially not connected)
    (closed_door R0 R4) (closed_door R0 R2) (closed_door R0 R3) (closed_door R1 R3) (closed_door R2 R0) (closed_door R2 R4) (closed_door R3 R1) (closed_door R3 R0) (closed_door R4 R0) (closed_door R4 R2) 
    ;Keys position and counter
    
    (= (key_counter) 0)
    ;Treasures position and value
    (treasure_at T0 R4) (treasure_at T1 R3) 
    (= (treasure_value T0) 30) (= (treasure_value T1) 40) 
    ;Enemies position and stats
    (enemy_at E0 R2) (enemy_at E1 R3)  
    (= (enemy_life E0) 30) (= (enemy_life E1) 50)  
    (= (enemy_strength E0) 30) (= (enemy_strength E1) 50) 
    ;Weapons position and strength
    (weapon_at W0 R1) (weapon_at W1 R4)  
    (= (weapon_strength W0) 30) (= (weapon_strength W1) 50) 
    ;Potions position and value
    (potion_at P0 R2) (potion_at P1 R3)  
    (= (potion_value P0) 10) (= (potion_value P1) 10) 
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
      (>= (hero_loot) 24)
      (> (hero_life) 0)
      (>= (defeated_enemy_counter) 0)
    )
  )
)