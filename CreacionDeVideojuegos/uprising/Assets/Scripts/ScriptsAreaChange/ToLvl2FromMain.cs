using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ToLvl2FromMain : MonoBehaviour
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
                SceneManager.LoadScene("Level2");
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
