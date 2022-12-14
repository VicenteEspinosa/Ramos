using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class FirefighterMovement : MonoBehaviour
{
    [SerializeField]
    private float speed;

    [SerializeField]
    private float rotationSpeed;

    [SerializeField]
    private Rigidbody2D rb;
    Quaternion toRotation;
    float verticalInput;
    float horizontalInput;

    void Update()
    {
        if (InteractWithItems.isInteracting)
        {
            horizontalInput = 0f;
            verticalInput = 0f;
        }
        else
        {
            horizontalInput = Input.GetAxis("Horizontal Firefighter");
            verticalInput = Input.GetAxis("Vertical Firefighter");
        }

        Vector2 movementDirection = new Vector2(horizontalInput, verticalInput);
        float inputMagnitude = Mathf.Clamp01(movementDirection.magnitude);
        movementDirection.Normalize();

        rb.MovePosition(rb.position + movementDirection * speed * Time.fixedDeltaTime);

        if (movementDirection != Vector2.zero)
        {
            toRotation = Quaternion.LookRotation(Vector3.forward, movementDirection);
        }
        transform.rotation = Quaternion.RotateTowards(transform.rotation, toRotation, rotationSpeed * Time.deltaTime);
    }
}
