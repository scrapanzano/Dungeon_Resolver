(define (problem ${instance_name})
  (:domain ${domain_name})
  (:objects
    ${room_list} - room
    ${key_list} - key
  )
  (:init
    ${start_room}
    ${exit_room}
    ${room_links}
    ${closed_doors}
    ${keys_location}
  )

  (:goal
    (and
      (escape)
    )
  )
)