using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using Unity.VisualScripting;
using UnityEngine.SceneManagement;

public class HealthsManager : MonoBehaviour
{

    public TextMeshProUGUI DetectiveHealth_Text;
    public TextMeshProUGUI FireManHealth_Text;

    GameObject Firefighter;
    GameObject Detective;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Detective)
        {
            PlayerPrefs.SetFloat("DH", Mathf.Max((float)Variables.Object(Detective).Get("Current Health"), 0));
        }
        else if (GameObject.FindGameObjectsWithTag("Detective").Length == 1)
        {
            Detective = GameObject.FindGameObjectsWithTag("Detective")[0];
        }
        else
        {
            SceneManager.LoadScene("LoseScene");
        }
        if (Firefighter)
        {
            PlayerPrefs.SetFloat("FH", Mathf.Max((float)Variables.Object(Firefighter).Get("Current Health"), 0));
        }
        else if (GameObject.FindGameObjectsWithTag("Firefighter").Length == 1)
        {
            Firefighter = GameObject.FindGameObjectsWithTag("Firefighter")[0];
        }
        else
        {
            SceneManager.LoadScene("LoseScene");
        }

        var DH = PlayerPrefs.GetFloat("DH");
        var FH = PlayerPrefs.GetFloat("FH");

        DetectiveHealth_Text.text = "" + DH;
        FireManHealth_Text.text = "" + FH;
    }
}
