import { useContext, useState } from "react";
import { Link, NavLink } from "react-router-dom";
import { FaBarsStaggered, FaXmark } from "react-icons/fa6";
import { AuthContext } from "../context/AuthProvider";
import logo from '../assets/logo.gif';
import '../App.css';

const Navbar = () => {
    const [isMenuOpen, setIsMenuOpen] = useState(false);
    const { user, logOut } = useContext(AuthContext) || {};

    const handleLogout = () => {
        logOut()
            .then(() => {
                // Sign-out successful.
            })
            .catch((error) => {
                console.log(error);
            });
    };

    const handleMenuToggler = () => {
        setIsMenuOpen(!isMenuOpen);
    };

    const navItems = [
        { path: "/", title: "Home" },
        { path: "/about", title: "About" },
        { path: "/docs", title: "Docs" },
    ];

    return (
        <header className="max-w-screen-2xl container mx-auto xl:px-24 px-2 border fixed">
            <nav className="flex justify-between items-center py-2">
                <a href="/" className="flex items-center gap-2 text-2xl">
                    <h1 className="mb-3 text-primary">AssistMe</h1>
                </a>
                            <div className="flex gap-4 left-1/2 relative ml-8  cursor-pointer">
                                <div className="flex -space-x-2 overflow-hidden">
                                    {user?.photoURL && (
                                        <img
                                            title="photo url"
                                            className="inline-block h-10 w-10 rounded-full"
                                            src={user?.photoURL}
                                            alt="User profile"
                                        />
                                    )}
                                    </div>
                            </div>

                <div className="block">
                    <button onClick={handleMenuToggler}>
                        {isMenuOpen ? (
                            <FaXmark className="w-5 h-5 text-primary/75" />
                        ) : (
                            <FaBarsStaggered className="w-5 h-5 text-primary/75" />
                        )}
                    </button>
                </div>
            </nav>
            <div className={`px-4 bg-black py-5 rounded-sm ${isMenuOpen ? "opacity-100" : "opacity-0 hidden"} transition-opacity duration-1000`}>
                <ul>
                    {navItems.map(({ path, title }) => (
                        <li key={path} className="text-base text-white first:text-white py-1">
                            <NavLink onClick={handleMenuToggler} to={path}>{title}</NavLink>
                        </li>
                    ))}
                    {!user ? (
                        <>
                            <li className="text-white py-1" onClick={handleMenuToggler}>
                                <Link to={"/docs"}>Docs</Link>
                            </li>
                            <li className="text-white py-1" onClick={handleMenuToggler}>
                                <Link to={"/contact-us"}>Contact us</Link>
                            </li>
                            <li className="text-white py-1" onClick={handleMenuToggler}>
                                <Link to="/login">Log in</Link>
                            </li>
                            <li className="text-white py-1" onClick={handleMenuToggler}>
                                <Link to="/sign-up">Sign up</Link>
                            </li>
                        </>
                    ) : (
                        <li className="text-white py-1" onClick={handleMenuToggler}>
                            <Link onClick={handleLogout}>Log Out</Link>
                        </li>
                    )}
                </ul>
            </div>
        </header>
    );
}

export default Navbar;
