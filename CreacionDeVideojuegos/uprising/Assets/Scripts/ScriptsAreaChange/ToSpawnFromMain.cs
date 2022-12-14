using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ToSpawnFromMain : MonoBehaviour
{
    public void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Detective") || collision.gameObject.CompareTag("Firefighter"))
        {
            SceneManager.LoadScene("Spawn");
        }
    }
}
