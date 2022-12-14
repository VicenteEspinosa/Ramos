using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SimpleNav : MonoBehaviour
{
    private GameObject moveto;
    public float speed;
    public float sightRange;

    private GameObject player;
    private GameObject player2;
    private float distance = 100000;
    private float distance2 = 100000;
    // Start is called before the first frame update
    void Start()
    {
        
    }

// Update is called once per frame
    void FixedUpdate()
    {
        if (!player)
        {
            player = GameObject.Find("Firefighter(Clone)");
        }
        if (!player2)
        {
            player2 = GameObject.Find("Detective(Clone)");
        }
        CheckDistances();

        if (distance<distance2)
        {          
            MoveTowards(player, distance);
        } else if (distance2 < distance){
            MoveTowards(player2, distance2);
        }
        
    }

    void CheckDistances()
    {
        if (player != null){
            distance = Vector2.Distance(transform.position, player.transform.position);
        } else {
            distance = 100000;
        }
            
        if (player2 != null){
            distance2 = Vector2.Distance(transform.position, player2.transform.position);
        } else {
            distance2 = 100000;
        }
    }

    void MoveTowards(GameObject jugador, float closeness)
    {
        Vector2 direction = jugador.transform.position - transform.position;
            direction.Normalize();
            float angle = Mathf.Atan2(direction.y, direction.x)* Mathf.Rad2Deg;
            
            if(closeness < sightRange)
            {
                GetComponent<Rigidbody2D>().MovePosition(Vector2.MoveTowards(this.transform.position, jugador.transform.position, speed * Time.deltaTime));
                transform.rotation = Quaternion.Euler(Vector3.forward * angle);
            }
    }
}
