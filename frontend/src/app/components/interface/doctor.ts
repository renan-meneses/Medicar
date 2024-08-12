import { UUID } from "crypto";
import { Specialty } from "./specialty";

export interface Doctor {
    _id: UUID;
    name: string;
    crm: number;
    email: string;
    phone:string;
    specialty:Specialty;

}