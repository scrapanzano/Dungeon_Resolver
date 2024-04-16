(define (problem instance_30_1229)
  (:domain simple_dungeon)
  (:objects
    R0 R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 R16 R17 R18 R19 R20 R21 R22 R23 R24 R25 R26 R27 R28 R29  - room
    K0 K1 K2 K3 K4 K5 K6 K7 K8 K9 K10  - key
  )
  (:init
    (at R14)
    (exit_room R24)
    (connected R2 R3) (connected R3 R2) (connected R3 R4) (connected R4 R3) (connected R4 R5) (connected R5 R4) (connected R5 R6) (connected R6 R5) (connected R6 R7) (connected R7 R6) (connected R7 R8) (connected R8 R7) (connected R8 R9) (connected R9 R8) (connected R9 R10) (connected R10 R9) (connected R15 R16) (connected R16 R15) (connected R16 R17) (connected R17 R16) (connected R19 R20) (connected R20 R19) (connected R20 R21) (connected R21 R20) (connected R21 R22) (connected R22 R21) (connected R22 R23) (connected R23 R22) (connected R24 R25) (connected R25 R24) (connected R25 R26) (connected R26 R25) (connected R26 R27) (connected R27 R26) (connected R28 R29) (connected R29 R28) 
    (closed_door R0 R1 K0) (closed_door R0 R29 K1) (closed_door R1 R2 K2) (closed_door R4 R23 K3) (closed_door R10 R11 K4) (closed_door R11 R12 K5) (closed_door R12 R13 K6) (closed_door R13 R14 K7) (closed_door R14 R15 K8) (closed_door R17 R18 K9) (closed_door R18 R19 K10) 
    (key_at K0 R29)(key_at K1 R1)(key_at K2 R0)(key_at K3 R3)(key_at K4 R9)(key_at K5 R10)(key_at K6 R11)(key_at K7 R15)(key_at K8 R13)(key_at K9 R19)(key_at K10 R17)
  )

  (:goal
    (and
      (escape)
    )
  )
)