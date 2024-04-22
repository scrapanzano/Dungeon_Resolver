(define (problem instance_30_42)
  (:domain simple_dungeon)
  (:objects
    R0 R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 R16 R17 R18 R19 R20 R21 R22 R23 R24 R25 R26 R27 R28 R29  - room
    T0 T1 T2 T3 T4 T5  - treasure
  )
  (:init
    (at R0)
    (exit_room R20)
    (connected R0 R2) (connected R1 R29) (connected R1 R8) (connected R2 R0) (connected R2 R4) (connected R3 R4) (connected R3 R5) (connected R4 R3) (connected R4 R2) (connected R5 R6) (connected R5 R3) (connected R5 R7) (connected R6 R5) (connected R6 R7) (connected R6 R11) (connected R7 R6) (connected R7 R8) (connected R7 R5) (connected R7 R9) (connected R8 R7) (connected R8 R10) (connected R8 R1) (connected R9 R10) (connected R9 R7) (connected R10 R9) (connected R10 R8) (connected R10 R12) (connected R11 R6) (connected R12 R13) (connected R12 R10) (connected R13 R12) (connected R13 R14) (connected R13 R15) (connected R14 R13) (connected R14 R15) (connected R14 R16) (connected R14 R29) (connected R15 R14) (connected R15 R16) (connected R15 R13) (connected R16 R15) (connected R16 R14) (connected R16 R18) (connected R18 R16) (connected R18 R20) (connected R19 R20) (connected R19 R21) (connected R20 R19) (connected R20 R21) (connected R20 R18) (connected R21 R20) (connected R21 R19) (connected R23 R24) (connected R23 R25) (connected R24 R23) (connected R25 R26) (connected R25 R23) (connected R25 R27) (connected R26 R25) (connected R26 R27) (connected R26 R28) (connected R27 R26) (connected R27 R25) (connected R28 R26) (connected R29 R1) (connected R29 R14) 
    (closed_door R0 R1) (closed_door R0 R28) (closed_door R1 R0) (closed_door R1 R3) (closed_door R2 R3) (closed_door R2 R8) (closed_door R3 R2) (closed_door R3 R1) (closed_door R4 R5) (closed_door R4 R6) (closed_door R5 R4) (closed_door R5 R21) (closed_door R6 R4) (closed_door R6 R8) (closed_door R7 R11) (closed_door R8 R6) (closed_door R8 R2) (closed_door R9 R24) (closed_door R10 R11) (closed_door R11 R10) (closed_door R11 R7) (closed_door R12 R14) (closed_door R14 R12) (closed_door R15 R17) (closed_door R16 R17) (closed_door R17 R16) (closed_door R17 R18) (closed_door R17 R15) (closed_door R17 R19) (closed_door R18 R17) (closed_door R18 R19) (closed_door R19 R18) (closed_door R19 R17) (closed_door R20 R22) (closed_door R21 R22) (closed_door R21 R5) (closed_door R22 R21) (closed_door R22 R23) (closed_door R22 R20) (closed_door R22 R24) (closed_door R23 R22) (closed_door R24 R25) (closed_door R24 R22) (closed_door R24 R26) (closed_door R24 R9) (closed_door R25 R24) (closed_door R26 R24) (closed_door R27 R28) (closed_door R27 R29) (closed_door R28 R27) (closed_door R28 R29) (closed_door R28 R0) (closed_door R29 R28) (closed_door R29 R27) 
    (key_at R7) (key_at R1) (key_at R15) (key_at R18) (key_at R5) 
    (= (key_counter) 0)
    (treasure_at T0 R4) (treasure_at T1 R6) (treasure_at T2 R7) (treasure_at T3 R9) (treasure_at T4 R23) (treasure_at T5 R28) 
    ( = (treasure_value T0) 15) ( = (treasure_value T1) 10) ( = (treasure_value T2) 15) ( = (treasure_value T3) 10) ( = (treasure_value T4) 5) ( = (treasure_value T5) 10) 
    (= (hero_loot) 0)
  )

  (:goal
    (and
      (escape) ( >= (hero_loot) 49)
    )
  )
)