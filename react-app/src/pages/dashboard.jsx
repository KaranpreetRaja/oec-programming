import Navbar from "../components/navbar";
import Card from "../components/card";
import { useParams } from "react-router-dom";
import { MdAbc } from "react-icons/md";
import { VscSymbolKeyword } from "react-icons/vsc";
import { VscWordWrap } from "react-icons/vsc";

export default function Dashboard() {
  const { uid } = useParams();

  return (
    <div>
      <Navbar logged={true} userId={uid} />
      <div className="bg-gray-50 w-screen h-screen flex flex-row bg-gradient-to-r from-indigo-500 via-purple-300 to-red-400">
        <div className="flex flex-col w-full p-16 ">
          <h2 className="text-2xl font-semibold">Welcome!</h2>
          <div className="flex w-full px-2 py-11 space-x-9">
            <Card
              user_id={uid}
              level={1}
              icon={<MdAbc size={80} color="gray" />}
            />
            <Card
              user_id={uid}
              level={2}
              icon={<VscWordWrap size={80} color="gray" />}
            />
            <Card
              user_id={uid}
              level={3}
              icon={<VscWordWrap size={80} color="gray" />}
            />
            <Card
              user_id={uid}
              level={4}
              icon={<VscSymbolKeyword size={80} color="gray" />}
            />
            <Card
              user_id={uid}
              level={5}
              icon={<VscSymbolKeyword size={80} color="gray" />}
            />
          </div>
        </div>
      </div>
    </div>
  );
}
