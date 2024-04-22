(define (problem instance_40_1229)
  (:domain simple_dungeon)
  (:objects
    R0 R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 R16 R17 R18 R19 R20 R21 R22 R23 R24 R25 R26 R27 R28 R29 R30 R31 R32 R33 R34 R35 R36 R37 R38 R39  - room
    T0 T1 T2 T3  - treasure
  )
  (:init
    (at R0)
    (exit_room R14)
    (connected R0 R39) (connected R0 R2) (connected R2 R3) (connected R2 R0) (connected R2 R4) (connected R3 R2) (connected R3 R4) (connected R4 R3) (connected R4 R5) (connected R4 R2) (connected R4 R6) (connected R5 R4) (connected R5 R7) (connected R6 R4) (connected R6 R25) (connected R7 R5) (connected R7 R9) (connected R7 R34) (connected R8 R10) (connected R9 R10) (connected R9 R7) (connected R9 R11) (connected R9 R12) (connected R10 R9) (connected R10 R11) (connected R10 R8) (connected R10 R12) (connected R11 R10) (connected R11 R12) (connected R11 R9) (connected R11 R13) (connected R12 R11) (connected R12 R13) (connected R12 R10) (connected R12 R9) (connected R13 R12) (connected R13 R14) (connected R13 R11) (connected R13 R15) (connected R14 R13) (connected R14 R15) (connected R15 R14) (connected R15 R13) (connected R15 R17) (connected R16 R18) (connected R17 R15) (connected R18 R16) (connected R18 R20) (connected R20 R21) (connected R20 R18) (connected R20 R22) (connected R21 R20) (connected R21 R22) (connected R21 R23) (connected R22 R21) (connected R22 R23) (connected R22 R20) (connected R22 R26) (connected R23 R22) (connected R23 R21) (connected R23 R25) (connected R24 R25) (connected R24 R26) (connected R25 R24) (connected R25 R26) (connected R25 R23) (connected R25 R27) (connected R25 R6) (connected R26 R25) (connected R26 R27) (connected R26 R24) (connected R26 R28) (connected R26 R22) (connected R27 R26) (connected R27 R25) (connected R27 R29) (connected R28 R29) (connected R28 R26) (connected R28 R30) (connected R29 R28) (connected R29 R27) (connected R29 R31) (connected R30 R28) (connected R31 R32) (connected R31 R29) (connected R31 R33) (connected R31 R39) (connected R32 R31) (connected R32 R33) (connected R33 R32) (connected R33 R34) (connected R33 R31) (connected R34 R33) (connected R34 R35) (connected R34 R7) (connected R35 R34) (connected R35 R37) (connected R37 R35) (connected R39 R0) (connected R39 R31) 
    (closed_door R0 R1) (closed_door R1 R0) (closed_door R1 R2) (closed_door R1 R3) (closed_door R1 R38) (closed_door R2 R1) (closed_door R3 R1) (closed_door R3 R5) (closed_door R4 R23) (closed_door R5 R6) (closed_door R5 R3) (closed_door R6 R5) (closed_door R6 R8) (closed_door R8 R9) (closed_door R8 R6) (closed_door R9 R8) (closed_door R14 R16) (closed_door R15 R16) (closed_door R16 R15) (closed_door R16 R17) (closed_door R16 R14) (closed_door R17 R16) (closed_door R17 R18) (closed_door R17 R19) (closed_door R18 R17) (closed_door R18 R19) (closed_door R19 R18) (closed_door R19 R20) (closed_door R19 R17) (closed_door R19 R21) (closed_door R20 R19) (closed_door R21 R19) (closed_door R23 R4) (closed_door R27 R36) (closed_door R29 R30) (closed_door R30 R29) (closed_door R30 R31) (closed_door R30 R32) (closed_door R31 R30) (closed_door R32 R30) (closed_door R32 R34) (closed_door R33 R35) (closed_door R34 R32) (closed_door R34 R36) (closed_door R35 R36) (closed_door R35 R33) (closed_door R36 R35) (closed_door R36 R37) (closed_door R36 R34) (closed_door R36 R38) (closed_door R36 R27) (closed_door R37 R36) (closed_door R37 R38) (closed_door R37 R39) (closed_door R38 R37) (closed_door R38 R39) (closed_door R38 R36) (closed_door R38 R1) (closed_door R39 R38) (closed_door R39 R37) 
    (key_at R4) (key_at R33) (key_at R23) (key_at R20) (key_at R15) (key_at R18) (key_at R16) 
    (= (key_counter) 0)
    (treasure_at T0 R24) (treasure_at T1 R32) (treasure_at T2 R37) (treasure_at T3 R39) 
    ( = (treasure_value T0) 5) ( = (treasure_value T1) 10) ( = (treasure_value T2) 10) ( = (treasure_value T3) 15) 
    (= (hero_loot) 0)
  )

  (:goal
    (and
      (escape) ( >= (hero_loot) 30)
    )
  )
)