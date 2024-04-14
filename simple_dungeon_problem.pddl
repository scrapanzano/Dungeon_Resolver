(define (problem instance_30_1300)
  (:domain simple_dungeon)
  (:objects
    R0 R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 R16 R17 R18 R19 R20 R21 R22 R23 R24 R25 R26 R27 R28 R29  - room
    K1 K2 K3 K4 K5 K6  - key
  )
  (:init
    (at R7)
    (exit_room R10)
    (connected R0 R1) (connected R0 R29) (connected R0 R2) (connected R0 R28) (connected R0 R5) (connected R1 R0) (connected R1 R2) (connected R1 R3) (connected R1 R29) (connected R2 R1) (connected R2 R3) (connected R2 R0) (connected R2 R4) (connected R3 R2) (connected R3 R1) (connected R3 R5) (connected R3 R11) (connected R4 R5) (connected R4 R2) (connected R4 R6) (connected R5 R4) (connected R5 R6) (connected R5 R3) (connected R5 R0) (connected R6 R5) (connected R6 R7) (connected R6 R4) (connected R6 R8) (connected R7 R6) (connected R7 R8) (connected R7 R9) (connected R8 R7) (connected R8 R9) (connected R8 R6) (connected R8 R10) (connected R9 R8) (connected R9 R10) (connected R9 R7) (connected R9 R11) (connected R10 R9) (connected R10 R11) (connected R10 R8) (connected R10 R12) (connected R11 R10) (connected R11 R12) (connected R11 R9) (connected R11 R13) (connected R11 R3) (connected R11 R27) (connected R12 R11) (connected R12 R13) (connected R12 R10) (connected R12 R14) (connected R13 R12) (connected R13 R14) (connected R13 R11) (connected R13 R15) (connected R14 R13) (connected R14 R15) (connected R14 R12) (connected R14 R16) (connected R15 R14) (connected R15 R16) (connected R15 R13) (connected R15 R17) (connected R16 R15) (connected R16 R17) (connected R16 R14) (connected R16 R18) (connected R17 R16) (connected R17 R18) (connected R17 R15) (connected R17 R19) (connected R18 R17) (connected R18 R19) (connected R18 R16) (connected R18 R20) (connected R19 R18) (connected R19 R20) (connected R19 R17) (connected R19 R21) (connected R20 R19) (connected R20 R21) (connected R20 R18) (connected R20 R22) (connected R21 R20) (connected R21 R22) (connected R21 R19) (connected R21 R23) (connected R22 R21) (connected R22 R23) (connected R22 R20) (connected R22 R24) (connected R23 R22) (connected R23 R24) (connected R23 R21) (connected R23 R25) (connected R24 R23) (connected R24 R25) (connected R24 R22) (connected R24 R26) (connected R25 R24) (connected R25 R26) (connected R25 R23) (connected R25 R27) (connected R26 R25) (connected R26 R27) (connected R26 R24) (connected R26 R28) (connected R27 R26) (connected R27 R25) (connected R27 R29) (connected R27 R11) (connected R28 R29) (connected R28 R26) (connected R28 R0) (connected R29 R28) (connected R29 R0) (connected R29 R27) (connected R29 R1) 
    (closed_door R3 R5 K1) (closed_door R9 R11 K2) (closed_door R10 R12 K3) (closed_door R12 R14 K4) (closed_door R18 R19 K5) (closed_door R23 R24 K6) 
    (key_at K1 R0)(key_at K2 R8)(key_at K3 R9)(key_at K4 R11)(key_at K5 R21)(key_at K6 R26)
  )

  (:goal
    (and
      (escape)
    )
  )
)