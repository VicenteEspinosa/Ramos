import React, {useEffect} from 'react';
import { Route, Routes } from 'react-router-dom';
import CustomNavbar from './components/CustomNavbar';
import Home from './components/Home';
import UserList from './components/users/UserList';
import Register from './components/users/Register';
import Login from './components/users/Login';
import Profile from './components/users/Profile';
import OtherProfile from './components/users/OtherProfile';
import LocationFinder from './components/locations/LocationFinder';
import Locations from './components/locations/Locations';
import Chat from './components/users/Chat';
import ChatList from './components/users/ChatList';
import { connectWebSocket } from './components/users/Messager';
import useAuth from './hooks/useAuth';


export default function AppRoutes({ client, setClient }) {
  return (
    <main>
      <CustomNavbar />
      <Routes>
        <Route index element={<Home />} />
        <Route path="session/register" element={<Register />} />
        <Route path="session/Login" element={<Login setClient={setClient}/>} />
        <Route path="users" element={<UserList />} />
        <Route path="users/profile" element={<Profile />} />
        <Route path="locations" element={<Locations />} />
        <Route path="findLocation" element={<LocationFinder />} />
        <Route path="users/:id" element={<OtherProfile />} />
        <Route path="chat/:id" element={<Chat client={ client } setClient={setClient}/>} />
        <Route path="chatList" element={<ChatList />} />
      </Routes> 
    </main>
  );
}