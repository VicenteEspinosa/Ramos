using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BossDoorArea : MonoBehaviour
{
    public GameObject killBossMessage;

    private GameObject killText;

    public void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.CompareTag("Detective") || collision.gameObject.CompareTag("Firefighter"))
        {
            int alive = PlayerPrefs.GetInt("BossAlive");
            if(alive == 1)
            {
                killText = Instantiate(killBossMessage, new Vector3(0, 0, 0), Quaternion.identity);
            }
            else
            {
                PlayerPrefs.SetInt("CanOpen", 1);
            }
        }
    }

    public void OnTriggerExit2D(Collider2D other)
    {
        if (killText)
        {
            Destroy(killText);
        }
    }
}
