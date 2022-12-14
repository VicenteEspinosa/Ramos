using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.VisualScripting;

public class BossCollision : MonoBehaviour
{
    [SerializeField]
    private float bulletDamage;

    [SerializeField]
    private float axeDamage;
    [SerializeField]
    private GameObject AxeAudio;

    bool isCollidingWithAxe = false;

    GameObject Firefighter;
    GameObject Detective;

    // Update is called once per frame
    void Update()
    {
        if (!Firefighter && GameObject.FindGameObjectsWithTag("Firefighter").Length == 1)
        {
            Firefighter = GameObject.FindGameObjectsWithTag("Firefighter")[0];
        }
        if (!Detective && GameObject.FindGameObjectsWithTag("Detective").Length == 1)
        {
            Detective = GameObject.FindGameObjectsWithTag("Detective")[0];
        }
        if (Firefighter && Detective)
        {
            if ((bool)Variables.Object(Firefighter).Get("CanMove") && Input.GetAxis("Atack Firefighter") != 0 && isCollidingWithAxe)
            {
                TakeDamage(axeDamage, gameObject);
                GameObject[] previousSoundArray = GameObject.FindGameObjectsWithTag("AxeSound");
                if (previousSoundArray.Length == 0)
                {
                    Instantiate<GameObject>(AxeAudio);
                }
            }
            if ((float)Variables.Object(gameObject).Get("Current Health") <= 0)
            {
                PlayerPrefs.SetInt("BossAlive", 0);
                Destroy(gameObject);
            }
        }
    }

    // Para colliders con isTrigger True
    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "Axe")
        {
            isCollidingWithAxe = true;
        }
    }

     private void OnTriggerExit2D(Collider2D collision)
    {
        if (collision.gameObject.tag == "Axe")
        {
            isCollidingWithAxe = false;
        }
    }

    public void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.tag == "Bullet")
        {
            TakeDamage(bulletDamage, gameObject);
            Destroy(collision.gameObject);
        }
        else if (collision.gameObject.tag == "Detective")
        {
            TakeDamage((float)Variables.Object(gameObject).Get("Damage"), Detective);
        }
        else if (collision.gameObject.tag == "Firefighter")
        {
            TakeDamage((float)Variables.Object(gameObject).Get("Damage"), Firefighter);
        }
    }

    public void TakeDamage(float damage, GameObject damageReceiver)
    {
        Variables.Object(damageReceiver).Set("Current Health", (float)Variables.Object(damageReceiver).Get("Current Health")
            - damage);
    }
}
