using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class BossFromLvl2 : MonoBehaviour
{
    public GameObject cluePrefab;

    private GameObject clueText;
    public void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Detective") || collision.gameObject.CompareTag("Firefighter"))
        {
            if (GameObject.FindGameObjectsWithTag("Clue").Length > 0)
            {
                clueText = Instantiate(cluePrefab, new Vector3(0, 0, 0), Quaternion.identity);
            }
            else
            {
                SceneManager.LoadScene("BossScene");
            }
        }
    }

    public void OnCollisionExit2D(Collision2D collision)
    {
        if (clueText)
        {
            Destroy(clueText);
        }
    }
}
