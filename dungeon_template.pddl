(define (problem ${instance_name})
  (:domain ${domain_name})
  (:objects
    ${room_list} - room
    ${door_list} - door
    ${key_list} - key
    ${enemy_list} - enemy
    ${treasure_list} - treasure
    ${weapon_list} - weapon
    ${potion_list} - potion
  )
  (:init
    
    ${safe_rooms}
    ${closed_doors}
    ${keys_position}
    ${enemies_position}
    ${enemis_life}
    ${enemies_strenght}
    ${treasures_position}
    ${potions_position}
    ${weapons_position}
    ${potions_value}
    ${weapons_strength}
    ${exit_room}
    ${initial_room}
    ${hero_life}
    ${max_hero_life}
    ${hero_strength}
    ${hero_loot}
    
    
  )
  (:goal
    (and
      ${hero_loot}
      ${hero_life}
      ${escape}
    )
  )
)