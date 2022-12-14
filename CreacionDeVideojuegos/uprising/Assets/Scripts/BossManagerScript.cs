using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BossManagerScript : MonoBehaviour
{
    void Start()
    {
        PlayerPrefs.SetInt("BossAlive", 1);
        PlayerPrefs.SetInt("CanOpen", 0);
    }
}
