import LoadingSpinner from "./components/LoadingSpinner";

// Makes a loading page while any page is being rendered
export default function Loading() {
    return <div className="flex flex-col justify-center items-center h-screen"> Loading <LoadingSpinner /> </div>
  }