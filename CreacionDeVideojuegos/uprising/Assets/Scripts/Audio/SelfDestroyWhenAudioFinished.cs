using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class SelfDestroyWhenAudioFinished : MonoBehaviour
{
    void Update()
    {
        if (!gameObject.GetComponent<AudioSource>().isPlaying)
        {
            Destroy(gameObject);
        }
    }
}
