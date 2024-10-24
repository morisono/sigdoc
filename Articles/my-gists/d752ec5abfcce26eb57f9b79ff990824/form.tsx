'use client';

import * as z from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { Button } from '@/app/components/ui/button';
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/app/components/ui/form';
import { Input } from '@/app/components/ui/input';
import { useToast } from '@/app/components/ui/use-toast';

const formSchema = z.object({
  nickname: z
    .string()
    .min(1, {
      message: '入力が必要です',
    })
    .max(60, {
      message: '最大60文字です',
    }),
  email: z
    .string()
    .min(1, {
      message: '入力が必要です',
    })
    .email({
      message: '不正な形式です',
    }),
});

export default function FormWidget() {
  const { toast } = useToast();
  const form = useForm<z.infer<typeof formSchema>>({
    mode: 'onChange',
    resolver: zodResolver(formSchema),
    defaultValues: {
      nickname: '',
      email: '',
    },
  });

  const onSubmit = async (values: z.infer<typeof formSchema>) => {
    const serverActions = new Promise((resolve) => setTimeout(resolve, 2000));

    return serverActions
      .then(() => {
        form.reset();
        toast({
          title: '送信しました',
        });
      })
      .catch(() => {
        toast({
          title: '送信に失敗しました',
        });
      });
  };

  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
        <FormField
          control={form.control}
          name="nickname"
          render={({ field }) => (
            <FormItem>
              <FormLabel>ニックネーム</FormLabel>
              <FormControl>
                <Input
                  type="text"
                  autoComplete="off"
                  placeholder=""
                  {...field}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <FormField
          control={form.control}
          name="email"
          render={({ field }) => (
            <FormItem>
              <FormLabel>メールアドレス</FormLabel>
              <FormControl>
                <Input
                  type="email"
                  autoComplete="email"
                  placeholder=""
                  {...field}
                />
              </FormControl>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button
          disabled={form.formState.isSubmitting || !form.formState.isValid}
          type="submit"
        >
          送信
        </Button>
      </form>
    </Form>
  );
}