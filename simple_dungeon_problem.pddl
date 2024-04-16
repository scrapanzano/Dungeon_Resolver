(define (problem instance_30_42)
  (:domain simple_dungeon)
  (:objects
    R0 R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 R16 R17 R18 R19 R20 R21 R22 R23 R24 R25 R26 R27 R28 R29  - room
    K0 K1 K2 K3 K4 K5 K6 K7 K8  - key
  )
  (:init
    (at R15)
    (exit_room R25)
    (connected R0 R1) (connected R0 R29) (connected R1 R0) (connected R1 R2) (connected R1 R24) (connected R2 R1) (connected R2 R3) (connected R3 R2) (connected R5 R6) (connected R6 R5) (connected R6 R29) (connected R7 R8) (connected R8 R7) (connected R9 R10) (connected R10 R9) (connected R10 R11) (connected R11 R10) (connected R12 R13) (connected R13 R12) (connected R14 R15) (connected R15 R14) (connected R15 R16) (connected R16 R15) (connected R16 R17) (connected R17 R16) (connected R18 R19) (connected R19 R18) (connected R23 R24) (connected R24 R23) (connected R24 R1) (connected R28 R29) (connected R29 R28) (connected R29 R0) (connected R29 R6) 
    (closed_door R3 R4 K0) (closed_door R4 R10 K1) (closed_door R8 R9 K2) (closed_door R13 R14 K3) (closed_door R17 R18 K4) (closed_door R19 R20 K5) (closed_door R21 R22 K6) (closed_door R22 R23 K7) (closed_door R27 R28 K8) 
    (key_at K0 R2)(key_at K1 R9)(key_at K2 R10)(key_at K3 R12)(key_at K4 R19)(key_at K5 R18)(key_at K6 R20)(key_at K7 R21)(key_at K8 R29)
  )

  (:goal
    (and
      (escape)
    )
  )
)