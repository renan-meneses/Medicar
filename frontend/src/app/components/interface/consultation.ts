import { UUID } from "crypto";
import { Doctor } from "./doctor";

export interface Consultation {
    _id: UUID;
    name: string;
    day:string;
    hourly:string;
    scheduling_date:string;
    doctor:Doctor;

}