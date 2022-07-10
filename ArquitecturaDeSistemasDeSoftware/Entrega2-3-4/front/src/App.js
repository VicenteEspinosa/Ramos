import './App.css';
import { React, useState, useEffect } from 'react'; 
import { BrowserRouter } from 'react-router-dom';
import AppRoutes from './AppRoutes';
import { AuthProvider } from './context/AuthProvider';

function App() {
  const [client, setClient] = useState(null);

  return (
    <BrowserRouter>
    <AuthProvider>
        <AppRoutes client={ client } setClient={setClient}/>
    </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
