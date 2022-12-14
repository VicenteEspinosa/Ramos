using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AnimatorHandler : MonoBehaviour
{
    [SerializeField]
    private int atackCooldownTime = 1;

    bool isAtacking = false;

    Animator animator;
    float endAtackCooldownTime = 0f;
    float horizontal;
    float vertical;
    float atack;

    // Start is called before the first frame update
    void Start()
    {
        animator = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        if (InteractWithItems.isInteracting)
        {
            horizontal = 0f;
            vertical = 0f;
            atack = 0f;
        }
        else
        {
            horizontal = Input.GetAxis("Horizontal Firefighter");
            vertical = Input.GetAxis("Vertical Firefighter");
            atack = Input.GetAxis("Atack Firefighter");
        }

        if (horizontal == 0  && vertical == 0)
        {
            animator.SetBool("IsMoving", false);
        }
        else
        {
            animator.SetBool("IsMoving", true);
        }

        if (Time.time > endAtackCooldownTime)
        {
            if (isAtacking)
            {
                animator.ResetTrigger("Atack");
                isAtacking = false;
            }
            if (atack > 0)
            {
                animator.SetTrigger("Atack");
                isAtacking = true;
                endAtackCooldownTime = Time.time + atackCooldownTime;
            }
        }
    }
}
