import { useState, useEffect } from "react";
import axios from '../../api/axios';
import Pager from "./Pager";

const USERS_PER_PAGE = 5;

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);

  const changeCurrentPage = (newPage) => {
    setCurrentPage(newPage)
  };

  useEffect(() => {
    let isMounted = true;
    const controller = new AbortController();

    const getUsers = async () => {
      try {
        const response = await axios.get('/users', {
          signal: controller.signal
        });
        isMounted && setUsers(response.data);
      } catch (err) {
        console.error(err);
      }
    }

    getUsers();

    return () => {
      isMounted = false;
      controller.abort();
    }
  }, [])

  return (
    <article className="margins">
      <h1 className="title">Users List</h1>
      {users?.length
        ? (
          <ul>
            {
              users.map((user, i) => {
                if (USERS_PER_PAGE * (currentPage - 1) <= i && i < USERS_PER_PAGE * currentPage) {
                  //if username is equal to the current user, don't show it
                  var username = JSON.parse(localStorage.getItem('user')).user.toString().toLowerCase()
                  if (user.username === username) {
                    return (
                      <li key={i}>
                        <a href="/users/profile">
                          {user.username}
                        </a>
                      </li>
                    );
                  }
                  else {
                    return (
                      <li key={i}>
                        <a href={`/users/${user._id}`}>
                          {user.username}
                        </a>
                      </li>
                    )
                  }
                }
                return null;
              })
            }
          </ul>
        ) : <p>No users to display</p>
      }
      <br />
      <Pager
        id="users-pagination"
        elementsCount={users.length}
        currentPage={currentPage}
        onChangeFunction={changeCurrentPage}
        perPage={USERS_PER_PAGE}
      />
      <br />
    </article>
  );
};

export default UserList;