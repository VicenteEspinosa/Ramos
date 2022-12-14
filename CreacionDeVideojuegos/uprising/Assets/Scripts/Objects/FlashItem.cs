using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FlashItem : MonoBehaviour
{
    float timer = 0.0f;
    bool isStartColor = true;
    [SerializeField]
    float timeStart = 1.0f;
    [SerializeField]
    float timeEnd = 0.4f;
    [SerializeField]
    Color startColor = new Color(1, 1, 1, 1);
    [SerializeField]
    Color endColor = new Color(0.5f, 0.5f, 0.5f, 1);

    void Update()
    {
        timer += Time.deltaTime;
        if (isStartColor && timer >= timeStart)
        {
            isStartColor = false;
            timer = 0.0f;
            setColor(startColor);
        }
        else if (!isStartColor && timer >= timeEnd)
        {
            isStartColor = true;
            timer = 0.0f;
            setColor(endColor);
        }
    }
    public void setColor(Color color)
    {
        SpriteRenderer mySprite = this.GetComponent<SpriteRenderer>();
        mySprite.color = color;
    }
}


