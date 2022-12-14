using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ProgressBar : MonoBehaviour
{
    [SerializeField]
    private Image content;
    [SerializeField]
    private int maximum = 100;
    [SerializeField]
    private float current = 0f;
    [SerializeField]
    private Text text;
    private bool started = false;
    bool progressPaused = false;
    private float timeToEnd = 3f;

    void Update()
    {
        if (!progressPaused && started)
        {
            current += Time.deltaTime / timeToEnd * maximum;
            GetCurrentFill();
        }
    }

    public void StartProgress(float time)
    {
        started = true;
        timeToEnd = time;
    }

    void GetCurrentFill()
    {
        float fillAmount = (float)current / (float)maximum;
        content.fillAmount = fillAmount;
        text.text = ((int)(fillAmount * maximum)).ToString() + "%";
        if (fillAmount >= 1)
        {
            SelfDestroy();
        }
    }

    void SelfDestroy()
    {
        Destroy(gameObject);
    }

    public void PauseProgress()
    {
        progressPaused = true;
    }

    public void ResumeProgress()
    {
        progressPaused = false;
    }
}
