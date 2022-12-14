using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Tutorial : MonoBehaviour
{
    public GameObject controls;
    public GameObject continueText;
    public GameObject clueText;
    public GameObject doorText;
    public GameObject finishText;

    float targetTime = 5.0f;
    bool showingContinue = false;
    int phase = 0;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (phase == 0 && targetTime <= 0.0f && Input.GetButtonDown("Space"))
        {
            controls.SetActive(false);
            continueText.SetActive(false);
            clueText.SetActive(true);
            phase += 1;
        }
        else if (phase == 1 && GameObject.FindGameObjectsWithTag("Clue").Length == 0)
        {
            clueText.SetActive(false);
            doorText.SetActive(true);
            phase += 1;
        }
        else if (phase == 2 && GameObject.FindGameObjectsWithTag("Door").Length == 0)
        {
            doorText.SetActive(false);
            finishText.SetActive(true);
            phase += 1;
            PlayerPrefs.SetInt("tutorial", 1);
        }
        
        if (targetTime <= 0.0f && !showingContinue)
        {
            showingContinue = true;
            continueText.SetActive(true);
        }
        else
        {
            targetTime -= Time.deltaTime;
        }
    }
}
