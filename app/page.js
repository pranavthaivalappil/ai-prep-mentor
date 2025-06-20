import Image from "next/image";
import { Button } from "../components/ui/button";

export default function Home() {
  return (
   <div className="p-8">
    <h2 className="text-2xl font-bold mb-4">Hello World</h2>
    <Button>Click me</Button>
   </div>
  );
}
