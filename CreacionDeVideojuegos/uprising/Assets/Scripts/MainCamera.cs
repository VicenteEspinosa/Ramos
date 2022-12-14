using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;
using UnityEngine.SceneManagement;

[RequireComponent(typeof(Camera))]
public class MainCamera : MonoBehaviour
{
    public Vector3 offset;
    public float smoothTime = .1f;
    public GameObject tutorialPrefab;
    public GameObject detectivePrefab;
    public GameObject firefighterPrefab;

    private List<Transform> targets;
    private Vector3 velocity;

    private void Start()
    {
        int tutorial = PlayerPrefs.GetInt("tutorial");
        if (tutorial == 0)
        {
            Instantiate(tutorialPrefab, new Vector3(0, 0, 0), Quaternion.identity);
        }
        GameObject detective = Instantiate(detectivePrefab, transform.localPosition + new Vector3(0, -1, 0), Quaternion.identity);
        GameObject firefighter = Instantiate(firefighterPrefab, transform.localPosition + new Vector3(0, 1, 0), Quaternion.identity);

        targets = new List<Transform>
        {
            detective.transform,
            firefighter.transform
        };
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.R))
        {
            SceneManager.LoadScene("MainMenu");
        }
    }

    private void LateUpdate()
    {
        if (targets.All(player => player == null))
        {
            return;
        }

        Transform firstTarget = targets.First(player => player != null);
        var bounds = new Bounds(firstTarget.position, Vector3.zero);
        for (int i = 0; i < targets.Count; i++)
        {
            if (targets[i] == null)
            {
                continue;
            }
            bounds.Encapsulate(targets[i].position);
        }

        Move(bounds);
    }

    private void Move(Bounds bounds)
    {

        Vector3 centerPoint = bounds.center;

        Vector3 newPosition = centerPoint + offset;
        transform.position = Vector3.SmoothDamp(transform.position, newPosition, ref velocity, smoothTime);
    }
}
