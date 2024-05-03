; First simple dungeon instance, with just one door, one enemy, one weapon, one potion, and one treasure.
;
; Dungeon representation is similar to:
;
; R1(S) - -  R2(T)(W)   R5 - | - R7(G)
;  \        /          /
;   \      /          /
;    R3(P) - - - R4(E) - - - R6(K) 
;
; S:start - G:exit(goal) - T:treasure - P:potion - E:enemy - K:key - W:weapon - |:door

(define (problem instance1_DG) (:domain dungeon)

;Objects and their hierarchy 
(:objects 
    R1 R2 R3 R4 R5 R6 R7 - room
    zombie - enemy
    coins - treasure 
    life_potion - potion
    sword - weapon
)

;Initial state's facts and numeric values
(:init
    ;Connected rooms (no door between them)
    (connected R1 R2) (connected R1 R3) (connected R2 R3) (connected R3 R4) (connected R4 R5) (connected R4 R6) 
    (connected R2 R1) (connected R3 R1) (connected R3 R2) (connected R4 R3) (connected R5 R4) (connected R6 R4) 
    ;Safe rooms (no enemies inside)
    (room_safe R1) (room_safe R2) (room_safe R3) (room_safe R5) (room_safe R6) (room_safe R7)
    ;Closed door between rooms (rooms are initially not connected)
    (closed_door R5 R7)
    ;Key position
    (key_at R6)
    (= (key_counter) 0)
    ;Enemy position and stats
    (enemy_at zombie R4)
    (= (enemy_life zombie) 30)
    (= (enemy_strength zombie) 30)
    ;Treasure position and value
    (treasure_at coins R2)
    (= (treasure_value coins) 10)
    ;Potion position and value
    (potion_at life_potion R3)
    (= (potion_value life_potion) 15)
    (= (potion_counter) 0)
    ;Weapon position and strength
    (weapon_at sword R2)
    (= (weapon_strength sword) 40)
    ;Dungeon exit room
    (exit_room R7)
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
    (>= (hero_loot) 10)
    (>= (hero_life) 80)
    (escape)
    )
)

;un-comment the following line if metric is needed
;(:metric minimize (???))
)
