using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
    class Program
    {
        static double calcularINSS(double sal)
        {
            double salario = sal;
            if (salario <= 1659.38f)
            {
                salario = sal + (sal * 0.08);
            }else if(salario >= 1659.39f && salario <= 2765.66f)
            {
                salario = sal + (sal * 0.09);
            }
            else if(salario >= 2765.67f && salario <= 5531.31f)
            {
                salario = sal + (sal * 0.11);
            }
            else
            {
                salario = sal - 608.44f;
            }
            return salario;
        }

        static double calcularHorasExtras(double sal, int horas)
        {

            return sal - ((((sal / 220) * 0.5) + (sal / 220)) * horas);
        }

        static double calcularAdicionalNoturno(double sal, int horas)
        {

            return sal - ((((sal / 220) * 0.2) + (sal / 220)) * horas);
        }

        static double calcularValeTransporte(double sal)
        {

            return sal - (sal * 0.06);
        }

        static double calcularIRPF(double sal)
        {
            double salario = sal;
            if(sal >= 1903.99f && sal <= 2826.65)
            {
                salario = (sal + (sal * 0.075))-142.80f;
            }
            else
            if (sal >= 2826.66 && sal <= 3751.05f)
            {
                salario = (sal + (sal * 0.15))-354.80f;
            }
            else
            if (sal >= 3751.06f && sal <= 4664.68f)
            {
                salario = (sal + (sal * 0.225))-636.13f;
            }
            else
            {
                salario = (sal + (sal * 0.275))-869.36f;
            }

            return salario;
        }

        static void Main(string[] args)
        {

            double salariob;
            int horasExtras;
            int horasExtrasNoturno;
            double gratificacao;
            double insalu;
            double pericu;
            string nome;
            string matricula;
            string cargo;
            string setor;

            bool test;

            Console.WriteLine("Nome: ");
            nome = Console.ReadLine();
            Console.WriteLine("Matricula: ");
            matricula = Console.ReadLine();
            Console.WriteLine("Cargo: ");
            cargo = Console.ReadLine();
            Console.WriteLine("Setor: ");
            setor = Console.ReadLine();


            do
            {
                Console.WriteLine("Digite o salario base");
                test = double.TryParse(Console.ReadLine(), out salariob);

            } while (test == false);

            do
            {
                Console.WriteLine("Horas extras realizadas no mes");
                test = int.TryParse(Console.ReadLine(), out horasExtras);

            } while (test == false);

            do
            {
                Console.WriteLine("Adicional noturno, horas");
                test = int.TryParse(Console.ReadLine(), out horasExtrasNoturno);

            } while (test == false);

            do
            {
                Console.WriteLine("Gratificação de função");
                test = double.TryParse(Console.ReadLine(), out gratificacao);

            } while (test == false);

            do
            {
                Console.WriteLine("Adicional de insalubridade");
                test = double.TryParse(Console.ReadLine(), out insalu);

            } while (test == false);

            do
            {
                Console.WriteLine("Adicional de periculosidade");
                test = double.TryParse(Console.ReadLine(), out pericu);

            } while (test == false);

            double salarioResultado = salariob;
            salarioResultado += calcularAdicionalNoturno(salariob, horasExtrasNoturno);
            salarioResultado += calcularHorasExtras(salariob, horasExtras);
            salarioResultado += (salariob * (insalu / 100));
            salarioResultado += (salariob * (pericu / 100));
            salarioResultado += (salariob * (gratificacao / 100));//calcular insalubridade
            salarioResultado = calcularINSS(salarioResultado);
            salarioResultado = calcularIRPF(salarioResultado);
            salarioResultado = calcularValeTransporte(salarioResultado);
                
            Console.WriteLine(salarioResultado);
            Console.ReadKey();
            
        }
    }
}
