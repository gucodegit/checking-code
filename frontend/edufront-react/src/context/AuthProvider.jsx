// AuthProvider.jsx - компонент-провайдер,
// экспортирует только компонент провайдера.
import { useState } from 'react';
import { AuthContext } from './AuthContext';

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  const login = (username, password, role, extra = {}) => {
    setUser({ username, role, ...extra });
  };

  const logout = () => {
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};