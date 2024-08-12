import { UUID } from "crypto";
import { Doctor } from "./doctor";

export interface Agenda{
    _id: UUID;
    doctor: Doctor;
    day: string;
    schedule: Array<string>;
}