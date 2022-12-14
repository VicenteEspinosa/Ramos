using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

public class InteractWithItems : MonoBehaviour

{
    public AudioSource doorsound;
    GameObject fireSound;
    [SerializeField]
    private GameObject FireSound;

    [HideInInspector]
    public static bool isInteracting;
    [SerializeField]
    float timeToUnlockDoor = 3;
    [SerializeField]
    float timeToExtinguishFire = 3;
    [SerializeField]
    float timeBetweenKeys = 1;
    float timeOfLastKey;
    bool waitingForKeyInput = false;
    [SerializeField]
    GameObject[] keys;
    [SerializeField]
    string[] keysMeaning;
    GameObject currentKey;
    string expectedInput;

    [HideInInspector]
    public GameObject progressBar;
    [SerializeField]
    GameObject CustomProgressBar;
    float startedInteractingTime;
    List<Collider2D> colliders = new List<Collider2D>();
    string[] collisionTags = {"Door", "Fire", "BossDoor"};
    Collider2D itemInteractingCollider;
    [SerializeField]
    bool pauseSoundWhenWaitingKey = false;


    // Start is called before the first frame update
    void Start()
    {
        isInteracting = false;
        if (!GameObject.FindGameObjectWithTag("Canvas"))
        {
            // Create a Canvas
            GameObject canvas = new GameObject("Canvas");
            canvas.tag = "Canvas";
            canvas.AddComponent<Canvas>();
            canvas.GetComponent<Canvas>().renderMode = RenderMode.WorldSpace;
        }
    }

    // Update is called once per frame
    void Update()
    {
        if (colliders.Count > 0 && !isInteracting)
        {
            // Start interacting
            if (Input.GetAxis("Interact Firefighter") != 0)
            {
                itemInteractingCollider = GetClosestCollider();
                if(!(itemInteractingCollider.gameObject.tag == "BossDoor"))
                {
                    timeOfLastKey = Time.time;
                    isInteracting = true;
                    startedInteractingTime = Time.time;
                    progressBar = GameObject.Instantiate(CustomProgressBar);
                    progressBar.transform.SetParent (GameObject.FindGameObjectWithTag("Canvas").transform, false);
                    if (itemInteractingCollider.gameObject.tag == "Door")
                    {
                        doorsound.Play();
                        progressBar.transform.position = itemInteractingCollider.transform.position;
                        progressBar.GetComponent<ProgressBar>().StartProgress(timeToUnlockDoor);
                    }
                    else if (itemInteractingCollider.gameObject.tag == "Fire")
                    {
                        fireSound = Instantiate<GameObject>(FireSound);
                        // set time of fireSound to time left to extinguish fire
                        fireSound.GetComponent<AudioSource>().time = fireSound.GetComponent<AudioSource>().clip.length - timeToExtinguishFire;
                        progressBar.transform.position = itemInteractingCollider.transform.position;
                        progressBar.GetComponent<ProgressBar>().StartProgress(timeToExtinguishFire);
                    }
                }
                else
                {
                    int sePuede = PlayerPrefs.GetInt("CanOpen");
                    if(sePuede == 1)
                    {
                        timeOfLastKey = Time.time;
                        isInteracting = true;
                        startedInteractingTime = Time.time;
                        progressBar = GameObject.Instantiate(CustomProgressBar);
                        progressBar.transform.SetParent (GameObject.FindGameObjectWithTag("Canvas").transform, false);
                        doorsound.Play();
                        progressBar.transform.position = itemInteractingCollider.transform.position;
                        progressBar.GetComponent<ProgressBar>().StartProgress(timeToUnlockDoor);
                    }
                }
            }
        }

        if (isInteracting)
        {
            if (progressBar == null)
            {
                isInteracting = false;

                Destroy(itemInteractingCollider.gameObject);
                colliders.Remove(itemInteractingCollider);
            }

            else if (!waitingForKeyInput && Time.time > timeOfLastKey + timeBetweenKeys)
            {
                CreateRandomKey();
                waitingForKeyInput = true;
                progressBar.GetComponent<ProgressBar>().PauseProgress();
                if (pauseSoundWhenWaitingKey)
                {
                    if (itemInteractingCollider.gameObject.tag == "Door")
                    {
                        doorsound.Pause();
                    }
                    else if (itemInteractingCollider.gameObject.tag == "Fire")
                    {
                        fireSound.GetComponent<AudioSource>().Pause();
                    }
                }
            }
            else if (waitingForKeyInput)
            {
                if (Input.GetKey(expectedInput))
                {
                    Destroy(currentKey);
                    timeOfLastKey = Time.time;
                    waitingForKeyInput = false;
                    progressBar.GetComponent<ProgressBar>().ResumeProgress();
                    if (pauseSoundWhenWaitingKey)
                    {
                        if (itemInteractingCollider.gameObject.tag == "Door")
                        {
                            doorsound.Play();
                        }
                        else if (itemInteractingCollider.gameObject.tag == "Fire")
                        {
                            fireSound.GetComponent<AudioSource>().Play();
                        }
                    }
                }
            }
        }
    }

    public void OnTriggerEnter2D(Collider2D collision)
    {
        if (collisionTags.Contains(collision.gameObject.tag))
        {
            colliders.Add(collision);
        }
    }

    public void OnTriggerExit2D(Collider2D collision)
    {
        if (collisionTags.Contains(collision.gameObject.tag))
        {
            colliders.Remove(collision);
        }
    }

    public void CreateRandomKey()
    {
        int randomIndex = Random.Range (0, keys.Length);
        currentKey = Instantiate<GameObject>(keys[randomIndex]);
        expectedInput = keysMeaning[randomIndex];
        currentKey.transform.position = new Vector3(transform.parent.position.x, transform.parent.position.y, transform.parent.position.z - 1);
    }

    Collider2D GetClosestCollider()
    {
        Collider2D closestCollider = null;
        float closestDistance = float.MaxValue;
        foreach (Collider2D collider in colliders)
        {
            float distance = Vector2.Distance(transform.position, collider.transform.position);
            if (distance < closestDistance)
            {
                closestDistance = distance;
                closestCollider = collider;
            }
        }
        return closestCollider;
    }
}
