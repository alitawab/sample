import { isRouteErrorResponse, useRouteError } from "react-router-dom";

export default function ErrorPage() {
    const error = useRouteError();
    console.error(error); // for dev purposes

    let title = "Something went wrong.";
    let description = "An unexpected error occured."
    if(isRouteErrorResponse(error)) {
        title = `${error.status} - ${error.statusText}`;
        description = "Sorry, we could not load the page.";
    }
    return (
        <div className='min-h-screen flex items-center justify-center bg-gray-50 p-8 text-center'>
            <div className='max-w-md space-y-4'>
                <h1 className='text-4xl font-bold text-red-600'>{title} 😕</h1>
                <p className='text-gray-700'>{description}</p>
                <a href='/' className='btn btn-outline'>Go back to Home</a>
            </div>
        </div>
    );
}

