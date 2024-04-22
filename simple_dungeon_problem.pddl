(define (problem instance_30_1229)
  (:domain simple_dungeon)
  (:objects
    R0 R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 R16 R17 R18 R19 R20 R21 R22 R23 R24 R25 R26 R27 R28 R29  - room
    relic_R20 rubies_R17 rubies_R5 diamonds_R14 coins_R26 relic_R2 coins_R11 diamonds_R28 diamonds_R24  - treasure
  )
  (:init
    (at R0)
    (exit_room R10)
    (connected R0 R1) (connected R0 R2) (connected R0 R28) (connected R1 R0) (connected R1 R3) (connected R2 R3) (connected R2 R0) (connected R3 R2) (connected R3 R4) (connected R3 R1) (connected R4 R3) (connected R4 R5) (connected R4 R6) (connected R4 R7) (connected R4 R19) (connected R4 R22) (connected R5 R4) (connected R5 R6) (connected R5 R7) (connected R6 R5) (connected R6 R4) (connected R6 R8) (connected R6 R12) (connected R7 R5) (connected R7 R4) (connected R8 R9) (connected R8 R6) (connected R8 R10) (connected R9 R8) (connected R10 R8) (connected R10 R12) (connected R11 R12) (connected R12 R11) (connected R12 R13) (connected R12 R10) (connected R12 R6) (connected R13 R12) (connected R13 R14) (connected R13 R15) (connected R14 R13) (connected R15 R16) (connected R15 R13) (connected R16 R15) (connected R16 R17) (connected R16 R18) (connected R17 R16) (connected R17 R18) (connected R18 R17) (connected R18 R19) (connected R18 R16) (connected R18 R20) (connected R19 R18) (connected R19 R21) (connected R19 R4) (connected R20 R21) (connected R20 R18) (connected R20 R22) (connected R21 R20) (connected R21 R22) (connected R21 R19) (connected R21 R23) (connected R22 R21) (connected R22 R23) (connected R22 R20) (connected R22 R4) (connected R23 R22) (connected R23 R21) (connected R23 R25) (connected R24 R25) (connected R24 R26) (connected R24 R27) (connected R25 R24) (connected R25 R23) (connected R26 R27) (connected R26 R24) (connected R27 R26) (connected R27 R29) (connected R27 R24) (connected R28 R0) (connected R29 R27) 
    (closed_door R0 R29) (closed_door R1 R2) (closed_door R1 R29) (closed_door R2 R1) (closed_door R2 R4) (closed_door R2 R23) (closed_door R3 R5) (closed_door R4 R2) (closed_door R5 R3) (closed_door R6 R11) (closed_door R7 R9) (closed_door R9 R10) (closed_door R9 R7) (closed_door R9 R11) (closed_door R10 R9) (closed_door R10 R11) (closed_door R11 R10) (closed_door R11 R9) (closed_door R11 R6) (closed_door R12 R14) (closed_door R14 R15) (closed_door R14 R12) (closed_door R14 R16) (closed_door R15 R14) (closed_door R15 R17) (closed_door R16 R14) (closed_door R17 R15) (closed_door R17 R19) (closed_door R19 R17) (closed_door R23 R2) (closed_door R25 R26) (closed_door R25 R27) (closed_door R26 R25) (closed_door R26 R28) (closed_door R27 R25) (closed_door R28 R29) (closed_door R28 R26) (closed_door R29 R28) (closed_door R29 R0) (closed_door R29 R1) 
    (key_at R4) (key_at R8) (key_at R9) (key_at R12) (key_at R23) (key_at R26) (key_at R27) 
    (= (key_counter) 0)
    (treasure_at relic_R20 R20) (treasure_at rubies_R17 R17) (treasure_at rubies_R5 R5) (treasure_at diamonds_R14 R14) (treasure_at coins_R26 R26) (treasure_at relic_R2 R2) (treasure_at coins_R11 R11) (treasure_at diamonds_R28 R28) (treasure_at diamonds_R24 R24) 
    (= (treasure_value relic_R20) 40) (= (treasure_value rubies_R17) 20) (= (treasure_value rubies_R5) 20) (= (treasure_value diamonds_R14) 30) (= (treasure_value coins_R26) 10) (= (treasure_value relic_R2) 40) (= (treasure_value coins_R11) 10) (= (treasure_value diamonds_R28) 30) (= (treasure_value diamonds_R24) 30) 
    (= (hero_loot) 0)
  )

  (:goal
    (and
      (escape) ( >= (hero_loot) 115)
    )
  )
)