using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Unity.VisualScripting;


public class CheckHealth : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if ((float)Variables.Object(gameObject).Get("Current Health") <= 0)
        {
            Destroy(gameObject);
        }
    }
}
