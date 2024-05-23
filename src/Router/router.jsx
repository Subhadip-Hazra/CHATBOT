import { createBrowserRouter } from "react-router-dom";
import App from "../App";
import Home from "../Pages/Home";
import About from "../Pages/About";
import Docs from "../Pages/Docs";
import Login from "../Pages/Login";
import Signup from "../Pages/SignUp";

const router = createBrowserRouter([
    {
        path: "/",
        element: <App/>,
        children:[
            {
                path: "/" ,
                element: <Home/>
            },
            {
                path: "/about",
                element: <About/>
            },
            {
                path: "/docs",
                element : <Docs/>
            }

        ],
    },
    {
        path: "/login",
        element:<Login/>
    },
    {
        path:"/sign-up",
        element:<Signup/>
    }
]);

export default router;