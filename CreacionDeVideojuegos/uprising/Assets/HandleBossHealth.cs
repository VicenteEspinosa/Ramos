using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using Unity.VisualScripting;


public class HandleBossHealth : MonoBehaviour
{
    [SerializeField]
    private Image content;
    [SerializeField]
    GameObject boss;

    void Update()
    {
        if (boss)
        {
            float fillAmount = (float)Variables.Object(boss).Get("Current Health") / (float)Variables.Object(boss).Get("Max Health");
            content.fillAmount = fillAmount;
        }
    }
}
