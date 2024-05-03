; A more complex dungeon instance, with different doors, enemies, weapons, potions, treasures.
; 
;Dungeon representation is similar to:
; 
; [R1(S)]- - -[R2(W)]- - -[R3(K)]
;    |                                  [R13(P)]- - -[R14(E)]- - -[R15(K)]
;   |D|                                /
;    |                                /
; [R4(E)]- - -[R11(E)]- |D| - [R12(T)]
;    |                                \
;    |                                 |D|
;    |                                   \ 
; [R5(T)]- - -[R6(P)]     [R10(W)]        [R16(T,W,P)]- - -[R17(E)]- - -[R18(G)]      
;    |                       |
;    |                       | 
; [R7(K)]- - -[R8(E)]- - -[R9(T)]
;
;
; S:start - G:exit(goal) - T:treasure - P:potion - E:enemy - K:key - W:weapon - |D|:door

(define (problem instance2_DG) (:domain dungeon)

;Objects and their hierarchy 
(:objects 
    R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 R16 R17 R18 - room
    zombie mummy wolfman vampire titan - enemy
    coins rubies diamonds legendary_relic - treasure 
    small_potion medium_potion big_potion - potion
    sword two_handed_sword legendary_sword - weapon
)

;Initial state's facts and numeric values
(:init
    ;Connected rooms (no door between them)
    (connected R1 R2) (connected R2 R3) (connected R4 R11) (connected R4 R5) (connected R5 R6) (connected R5 R7) (connected R7 R8) (connected R8 R9) (connected R9 R10)
    (connected R2 R1) (connected R3 R2) (connected R11 R4) (connected R5 R4) (connected R6 R5) (connected R7 R5) (connected R8 R7) (connected R9 R8) (connected R10 R9)
    (connected R12 R13) (connected R13 R14) (connected R14 R15) (connected R16 R17) (connected R17 R18) 
    (connected R13 R12) (connected R14 R13) (connected R15 R14) (connected R17 R16) (connected R18 R17)
    ;Safe rooms (no enemies inside)
    (room_safe R1) (room_safe R2) (room_safe R3) (room_safe R5) (room_safe R6) (room_safe R7) (room_safe R9)
    (room_safe R10) (room_safe R12) (room_safe R13) (room_safe R15) (room_safe R16) (room_safe R18)
    ;Closed door between rooms (rooms are initially not connected)
    (closed_door R1 R4) (closed_door R11 R12) (closed_door R12 R16)
    ;Keys position
    (key_at R3) (key_at R7) (key_at R15)
    (= (key_counter) 0)
    ;Enemies position and stats
    (enemy_at zombie R4) (= (enemy_life zombie) 30) (= (enemy_strength zombie) 30)
    (enemy_at mummy R8) (= (enemy_life mummy) 30) (= (enemy_strength mummy) 30)
    (enemy_at wolfman R11) (= (enemy_life wolfman) 50) (= (enemy_strength wolfman) 50)
    (enemy_at vampire R14) (= (enemy_life vampire) 40) (= (enemy_strength vampire) 40)
    (enemy_at titan R17) (= (enemy_life titan) 90) (= (enemy_strength titan) 90)
    ;Treasures position and value
    (treasure_at coins R5) (= (treasure_value coins) 20)
    (treasure_at rubies R9) (= (treasure_value rubies) 30)
    (treasure_at diamonds R12) (= (treasure_value diamonds) 50)
    (treasure_at legendary_relic R16) (= (treasure_value legendary_relic) 100)
    ;Potions position and value
    (potion_at small_potion R6) (= (potion_value small_potion) 30)
    (potion_at medium_potion R13) (= (potion_value medium_potion) 50)
    (potion_at big_potion R16) (= (potion_value big_potion) 70)
    (= (potion_counter) 0)
    ;Weapons position and strength
    (weapon_at sword R2) (= (weapon_strength sword) 30)
    (weapon_at two_handed_sword R10) (= (weapon_strength two_handed_sword) 50)
    (weapon_at legendary_sword R16) (= (weapon_strength legendary_sword) 100)
    ;Dungeon exit room
    (exit_room R18)
    ;Hero initial position and stats
    (at R1)
    (= (hero_life) 100)
    (= (max_hero_life) 100)
    (= (hero_strength) 0)
    (= (hero_loot) 0)
    (= (defeated_enemy_counter) 0)
)

;Goal condition
(:goal (and
    (>= (hero_loot) 200)
    (> (hero_life) 0)
    (escape)
    )
)

;un-comment the following line if metric is needed
;(:metric minimize (???))
)
