(define (problem instance_30_1229)
  (:domain simple_dungeon)

  ;Objects and their hierarchy 
  (:objects
    R0 R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 R16 R17 R18 R19 R20 R21 R22 R23 R24 R25 R26 R27 R28 R29  - room
    T0 T1 T2 T3 T4 T5 T6 T7 T8  - treasure
    E0 E1 E2 E3 E4 E5  - enemy 
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
    (room_safe R0) (room_safe R2) (room_safe R3) (room_safe R4) (room_safe R5) (room_safe R6) (room_safe R7) (room_safe R9) (room_safe R10) (room_safe R11) (room_safe R12) (room_safe R13) (room_safe R14) (room_safe R15) (room_safe R17) (room_safe R19) (room_safe R20) (room_safe R21) (room_safe R22) (room_safe R23) (room_safe R26) (room_safe R27) (room_safe R28) (room_safe R29)  
    ;Closed door between rooms (rooms are initially not connected)
    (closed_door R0 R29) (closed_door R1 R2) (closed_door R1 R29) (closed_door R2 R1) (closed_door R2 R4) (closed_door R2 R23) (closed_door R3 R5) (closed_door R4 R2) (closed_door R5 R3) (closed_door R6 R11) (closed_door R7 R9) (closed_door R9 R10) (closed_door R9 R7) (closed_door R9 R11) (closed_door R10 R9) (closed_door R10 R11) (closed_door R11 R10) (closed_door R11 R9) (closed_door R11 R6) (closed_door R12 R14) (closed_door R14 R15) (closed_door R14 R12) (closed_door R14 R16) (closed_door R15 R14) (closed_door R15 R17) (closed_door R16 R14) (closed_door R17 R15) (closed_door R17 R19) (closed_door R19 R17) (closed_door R23 R2) (closed_door R25 R26) (closed_door R25 R27) (closed_door R26 R25) (closed_door R26 R28) (closed_door R27 R25) (closed_door R28 R29) (closed_door R28 R26) (closed_door R29 R28) (closed_door R29 R0) (closed_door R29 R1) 
    ;Keys position and counter
    (key_at R4) (key_at R8) (key_at R9) (key_at R12) (key_at R23) (key_at R26) (key_at R27) 
    (= (key_counter) 0)
    ;Treasure position and value
    (treasure_at T0 R20) (treasure_at T1 R17) (treasure_at T2 R5) (treasure_at T3 R14) (treasure_at T4 R26) (treasure_at T5 R2) (treasure_at T6 R11) (treasure_at T7 R28) (treasure_at T8 R24) 
    (= (treasure_value T0) 40) (= (treasure_value T1) 20) (= (treasure_value T2) 20) (= (treasure_value T3) 30) (= (treasure_value T4) 10) (= (treasure_value T5) 40) (= (treasure_value T6) 10) (= (treasure_value T7) 30) (= (treasure_value T8) 30) 
    ;Enemy position and stats
    (enemy_at E0 R1) (enemy_at E1 R25) (enemy_at E2 R8) (enemy_at E3 R24) (enemy_at E4 R18) (enemy_at E5 R16)  
    (= (enemy_life E0) 90) (= (enemy_life E1) 50) (= (enemy_life E2) 90) (= (enemy_life E3) 90) (= (enemy_life E4) 50) (= (enemy_life E5) 30)  
    (= (enemy_life E0) 90) (= (enemy_life E1) 50) (= (enemy_life E2) 90) (= (enemy_life E3) 90) (= (enemy_life E4) 50) (= (enemy_life E5) 30)  
    ;Hero initial stats
    (= (hero_loot) 0)
  )

  ;Goal condition
  (:goal
    (and
      (escape) (>= (hero_loot) 115)
    )
  )
)